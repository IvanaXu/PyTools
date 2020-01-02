# zip
# enumerate
# items

for i, j in zip([1,2,3], [2,2,3]):
    print(i, j)
# 1 2
# 2 2
# 3 3

for i, j in enumerate([43,23,54]):
    print(i, j)
# 0 43
# 1 23
# 2 54

for i, j in {1: 0, 3: 2, 2: 0}.items():
    print(i, j)
# 1 0
# 3 2
# 2 0


