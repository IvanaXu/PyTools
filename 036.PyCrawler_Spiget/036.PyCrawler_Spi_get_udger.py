# -*- coding:utf-8 -*-
# @auth ivan
# @time 2016-10-11 19:51:15
# @goal spider the udger by the proxies_ip
# url = 'https://udger.com/resources/ua-list#Browser'
import redis
from pyquery import PyQuery as pq
import requests
import random

r1 = redis.Redis(port=6379, host='', password='', db=0)
# redis
s = requests.session()
url = 'http://udger.com/resources/ua-list'
url_UA = 'url_UA'
list_UA = 'list_UA'


class Get_UA_List:
    def __init__(self):
        self.seqlist = []
        self.urlheader = 'http://udger.com'
        self.begin_s = '/resources/ua-list/browser-detail?browser=360 browser'
        self.end_s = '/resources/ua-list/browser-detail?browser=ZipZap'
        print('Start query_url')
        self.query_url()

    def query_url(self):
        text = s.get(url).content
        seqdata = pq(text)
        temp = seqdata('a')
        for i in range(len(temp)):
            j = temp.eq(i).attr('href')
            self.seqlist.append(j)

    def save_url(self):
        begin_num = self.seqlist.index(self.begin_s)
        end_num = self.seqlist.index(self.end_s)
        savelist = []
        for i in self.seqlist[begin_num:end_num + 1]:
            savelist.append(self.urlheader + i)

        print(savelist)
        print('Saving')
        p = r1.pipeline()
        for i in savelist:
            p.lpush(url_UA, i)
        p.execute()
        print('Finished')
# A = Get_UA_List()
# A.save_url()


def func(iurl, ip):
    text = s.get(iurl).content
    proxies = {
        'http': ip,
    }
    seqdata = pq(text)
    seqlist = []
    temp = seqdata('a')
    for i in range(len(temp)):
        j = temp.eq(i).attr('href')
        try:
            if j:
                if j.find('Fuas') != -1:
                    seqlist.append(j.split('Fuas=')[1])
        except Exception as e:
            print(e)
            continue

    print(seqlist)
    print('Saving')
    p = r1.pipeline()
    for i in seqlist:
        p.lpush('list_UA', i)
    p.execute()
    print('Finished')

urlist_UA = r1.lrange(url_UA, 0, r1.llen(url_UA))
proxies_ip = list(r1.smembers('proxies_ip_live'))
j = 0

for i in urlist_UA:
    print(j)
    ip = proxies_ip[random.randint(0, len(proxies_ip)-1)]
    func(i, ip)

    j += 1
    # break

