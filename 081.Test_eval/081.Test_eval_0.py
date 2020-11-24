# -*-coding:utf-8-*-
# @auth ivan
# @time 20201124 00:56:00
# @goal Test eval

print(eval("1+1"))
assert eval("1+1") == 2

a = 1
print(eval("a+1"))
assert eval("a+1") == a+1

import os
os.system("ls -l")
