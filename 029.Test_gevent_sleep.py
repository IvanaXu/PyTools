# -*-coding:utf-8-*-
# @auth ivan
# @time 20191029 ///
# @goal test for gevent sleep

from gevent import monkey
monkey.patch_all()
import gevent
import time
import random


def sleep(i, sleeptime):
    sleeptimes = 0

    sleeptimes = sleeptimes + sleeptime
    time.sleep(sleeptime)

    sleeptime1 = random.randint(sleeptime, 2)
    sleeptimes = sleeptimes + sleeptime1
    time.sleep(sleeptime)

    sleeptime2 = random.uniform(sleeptime1, 2)
    sleeptimes = sleeptimes + sleeptime2

    time.sleep(sleeptimes)
    print(i, sleeptimes)

time0 = time.time()

for j in range(1):
    spawnlist = []
    for i in range(9999):
        sleeptime = random.randint(1, 2)
        spawnlist.append(gevent.spawn(sleep, i, sleeptime))
    gevent.joinall(spawnlist)
    print('%d Task%d Time = %f' % (i+1, j+1, time.time() - time0))
# 9999 Task1 Time = 10.289901

