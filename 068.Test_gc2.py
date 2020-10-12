#
# gc 垃圾回收
import gc
import sys
gc.set_debug(gc.DEBUG_STATS)

a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
b.append(a)
del b
print(gc.collect())
print("END")

# gc: collecting generation 2...
# gc: objects in each generation: 833 493 4500
# gc: objects in permanent generation: 0
# gc: done, 24 unreachable, 0 uncollectable, 0.0009s elapsed
# 24
# END
