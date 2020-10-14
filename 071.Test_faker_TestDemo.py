# -*-coding:utf-8-*-
# @auth ivan
# @time 20201014
# @goal test faker

from faker import Faker
f0, f1, f2 = Faker("zh_CN"), Faker("ko_KR"), Faker()
pf = lambda f: print(f"\nname:{f.name()}\naddr:{f.address()}\njobs:{f.job()}\ncomp:{f.company()}")
pf(f0), pf(f1)

print(
    "\n",
    f2.safari(),
    "\n",
    f2.credit_card_full(),
)
"""
name:陈婷
addr:河南省张家港县黄浦杨路w座 611935
jobs:政府事务管理
comp:新宇龙信息科技有限公司

name:김진호
addr:대구광역시 성동구 선릉가 (영미백면)
jobs:성직자
comp:박김

 Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/531.22.3 (KHTML, like Gecko) Version/5.1 Safari/531.22.3 
 VISA 16 digit
Dawn Phillips
4648674864039732 06/29
CVC: 543
"""
