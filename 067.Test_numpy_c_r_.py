#
import numpy as np

a = np.random.randint(0, 10, size=(2, 2))
b = np.random.randint(0, 10, size=(2, 2))

print(a)
print(b)
print("r_\n", np.r_[a, b])
print("c_\n", np.c_[a, b])

# [[5 3]
#  [3 2]]
# [[0 1]
#  [8 4]]
# r_
#  [[5 3]
#  [3 2]
#  [0 1]
#  [8 4]]
# c_
#  [[5 3 0 1]
#  [3 2 8 4]]
