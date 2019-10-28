# -*- coding:utf-8 -*-
# @auth ivan
# @time 2016-10-11 21:58:06
# @goal get_ by proxies
# proxies url = 'http://www.66ip.cn/areaindex_19/index.html'

from gevent import monkey, Timeout
import gevent
import requests
from pyquery import PyQuery as pq
import redis
import time
import datetime
import logging
monkey.patch_all()

r1 = redis.Redis(port=6379, host='', db=0, password='')
# redis
s = requests.session()
ip_pool = 'proxies_ip_pool'
ip_live = 'proxies_ip_live'
url = 'http://www.66ip.cn/areaindex_19/index.html'
test_url = 'http://www.baidu.com'
path = '/ivan/python27/tPatterns/others/User-Agent/'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=path+'spi_get_proxies.log',
                    filemode='a+')


class Task_get:
    def __init__(self):
        pool_list = r1.smembers(ip_pool)
        p = r1.pipeline()
        for i in pool_list:
            p.srem(ip_pool, i)
        p.execute()

    def get_proxies_ip(self):
        seqlist = []
        text = s.get(url).content
        seqdata = pq(text)

        temp = seqdata('tr')
        for i in range(len(temp)):
            j = temp.eq(i).text()
            try:
                if i > 3:
                    proxies_url = 'http://' + j.split(' ')[0] + ':' + j.split(' ')[1]
                    seqlist.append(proxies_url)
            except Exception as e:
                logging.error(str(e))
                continue
        logging.info('get the proxies ip')
        return seqlist

    def save_proxies_ip(self):
        p = r1.pipeline()
        for i in self.get_proxies_ip():
            p.sadd(ip_pool, i)
        p.scard(ip_pool)
        return p.execute()[-1]
# A = Task_get()
# A.save_proxies_ip()


class Task_test:
    def __init__(self):
        live_list = r1.smembers(ip_live)
        p = r1.pipeline()
        for i in live_list:
            p.srem(ip_live, i)
        p.execute()

    def test_func(self, ip):
        proxies = {'http': ip}
        try:
            code = s.get(test_url, proxies=proxies).status_code
            if code == 200:
                print(ip, 'live')
                r1.sadd(ip_live, ip)
            else:
                raise Exception('Visit 500')
        except Exception as e:
            logging.error(str(e))

    def test(self):
        p = r1.pipeline()
        p.smembers(ip_pool)
        test_set = p.execute()[0]
        print('please wait')
        spawnlist = []
        for i in test_set:
            spawnlist.append(gevent.spawn(self.test_func, i))
        gevent.joinall(spawnlist)
# B = Task_test()
# B.tPatterns()


class Task_run(Task_get, Task_test):
    def __init__(self):
        Task_get.__init__(self)
        self.time_get = lambda: {
            'day': datetime.datetime.now().day,
            'hour': datetime.datetime.now().hour,
            'mins': datetime.datetime.now().minute,
        }
        self.time0 = self.time_get()
        self.sleep_time = 90

    def run(self):
        while True:
            # A  B
            # A0 B0/1
            # A1 B0
            # A1 B1
            # if self.time0['day'] != self.time_get()['day']:
            #     Task_get.save_proxies_ip(self)
            #     self.time0 = self.time_get()
            #
            # elif self.time0['hour'] != self.time_get()['hour']:
            #     Task_test.tPatterns(self)
            #     self.time0 = self.time_get()
            #
            # elif self.time0['mins'] != self.time_get()['mins']:
            if self.time0['hour'] != self.time_get()['hour']:
                Task_get.__init__(self)
                Task_get.save_proxies_ip(self)

                Task_test.__init__(self)
                Task_test.test(self)
                self.time0 = self.time_get()

            else:
                self.time0 = self.time_get()
            logging.info('Sleeping in 90s')
            time.sleep(self.sleep_time)

    def run_test(self):
        # Task_get.save_proxies_ip(self)
        Task_test.__init__(self)
        Task_test.test(self)

C = Task_run()
C.run()

