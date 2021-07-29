# 1
a = {1:0, 2:0}
b = {2:1, 3:1}
print(a|b)
# {1: 0, 2: 1, 3: 1}

a|=b
print(a)
# {1: 0, 2: 1, 3: 1}

# 2
import random
print(random.Random().randint(0,11))
# 9
print(random.Random().randbytes(12))
# b'\x90?w2J3\r\x18R\x8d\x96\xd1'

# 3
s1 = "S_"
s2 = f"{s1}XXX"
print(s2)
# 'S_XXX'
print(s2.startswith(s1))
# True
print(s2.removeprefix(s1))
# 'XXX'
print(s2)
# 'S_XXX'
print(s2.removeprefix(s1+"1"))
# 'S_XXX'