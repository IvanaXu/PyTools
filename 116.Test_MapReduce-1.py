from functools import reduce

L0 = [1, 2, 3]

L1 = list(map(lambda x: x*x, L0))
L2 = reduce(lambda x, y: x+y, L1)
print(L0, L1, L2)
# [1, 2, 3] [1, 4, 9] 14
