# -*- coding:utf-8 -*-
# @auth ivan
# @time 20190101
# @goal test the telnet
import telnetlib
import time
import random

h, p, n = "0.0.0.0", 11111, 0
while True:
    time.sleep(random.randrange(0, 1000) / 1000)
    n += 1
    try:
        tb = telnetlib.Telnet()
        tb.open(host=h, port=p, timeout=1)
        print("Step %5d" % n, tb.read_very_eager().decode(), "-" * 20)
        tb.close()
    except Exception as e:
        print("Fail %5d" % n, e)
