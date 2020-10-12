#
import numpy as np

a = np.random.randint(0, 10, size=(2, 2))
b = np.random.randint(0, 10, size=(2, 2))

print(a)
print(b)
print("r_\n", np.r_[a, b])
print("c_\n", np.c_[a, b])
print(a.ravel(), a.flatten())

# [[3 2]
#  [8 5]]

# [[6 5]
#  [1 6]]

# r_
#  [[3 2]
#  [8 5]
#  [6 5]
#  [1 6]]

# c_
#  [[3 2 6 5]
#  [8 5 1 6]]

# [3 2 8 5] [3 2 8 5]