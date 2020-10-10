# -*-coding:utf-8-*-
# @auth ivan
# @time 20191022 01:40:11
# @goal Be Pythonic
"""
| 01.checkin
| 02.for_look
| 03.merge
"""

# 01.checkin X >> Y
# 01.checkin X
dictionary = {"A": 1, "B": 2, "C": 3}
keys = dictionary.keys()
for k in keys:
    if "A" == k:
        print(True)
        break

# 01.checkin Y
dictionary = {"A": 1, "B": 2, "C": 3}
print(True if "A" in dictionary else False)

# 02.for_look X >> Y
# 02.for_look X
d = {i: i * 2 for i in range(10000)}
for key in d:
    print("{0} = {1}".format(key, d[key]))

# 02.for_look Y
d = {i: i * 2 for i in range(10000)}
for key, value in d.items():
    print("{0} = {1}".format(key, value))

# 03.merge X >> Y
# 03.merge X
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = dict(list(x.items()) + list(y.items()))
print(z)

# 03.merge Y1
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)

# 03.merge Y2
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = x.copy()
z.update(y)
print(z)
