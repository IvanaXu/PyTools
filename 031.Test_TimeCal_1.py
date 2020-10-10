# -*-coding:utf-8-*-
# @auth ivan
# @time 20191022 02:10:11
# @goal TimeCal
import time
import timeit

n = 100
x = {i: i**2 for i in range(0, 2 * n)}
y = {i: i**3 for i in range(n, 3 * n)}
z = {i: i**3 for i in range(0, 3 * n)}
f1 = lambda: {**x, **y}
f2 = lambda: {**x, **z}

t0 = time.time()
f1()
t1 = time.time()
print("f1 Use Time: %f" % (t1 - t0))

t0 = time.time()
f2()
t1 = time.time()
print("f2 Use Time: %f" % (t1 - t0))

print(min(timeit.repeat(f1)))
print(min(timeit.repeat(f2)))

# f1 Use Time: 0.000017
# f2 Use Time: 0.000009
# 7.1042271729093045
# 8.576795244123787
