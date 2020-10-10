# -*-coding:utf-8-*-
# @auth ivan
# @time 20191022 01:25:11
# @goal test for gevent requests
from gevent import monkey
monkey.patch_all()
import gevent
import requests


def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    print(resp)


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])

# GET: https://www.python.org/
# GET: https://www.yahoo.com/
# GET: https://github.com/
# <Response [200]>
# <Response [200]>
# <Response [200]>
