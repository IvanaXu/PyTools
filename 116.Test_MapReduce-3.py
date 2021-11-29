import time
import random
from functools import reduce

N = 10000
L = list(range(N)) + [N] + list(range(N))
random.shuffle(L)

def test1():
   for i in set(L):
      if L.count(i) == 1:
         return i

time0 = time.time()
assert N == test1()
timet1 = time.time() - time0
print(f"Time {timet1:.8f}s")

time0 = time.time()
assert N == reduce(lambda a, b:a^b, L)
timet2 = time.time() - time0
print(f"Time {timet2:.8f}s")

print(f"UP {timet1/timet2:f}")

"""
Time 3.14373922s
Time 0.00199342s
UP 1577.059921
"""