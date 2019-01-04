# -*-coding:utf-8-*-
# @auth ivan
# @time 20180706 10:58
# @goal test the socket server.
# TODO：HOW TO BUILD THE SERVER.
import requests

print('--1--')
s1 = requests.session()
r = s1.get('http://www.baidu.com')
print(r.text.encode('utf-8'))
s1.close()

print('--2--')
# pip install requests[socks]
proxies = {
    'http': 'socks5://user:user@58.87.77.225:8080',
    'https': 'socks5://user:user@58.87.77.225:8080'
}
s2 = requests.session()
r = s2.get('http://www.baidu.com', proxies=proxies)
print(r.text.encode('utf-8'))
s2.close()

print('--3--')
# pip install requests[socks]
proxies = {
    'http': 'socks5://user:user@47.93.21.40:8088',
    'https': 'socks5://user:user@47.93.21.40:8088'
}
s2 = requests.session()
r = s2.get('http://www.baidu.com', proxies=proxies)
print(r.text.encode('utf-8'))
s2.close()



