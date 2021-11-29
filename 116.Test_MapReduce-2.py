import pandas as pd
from functools import reduce

data1 = pd.DataFrame([[0, 1], [1, ]], columns=["A", "X1"])
print(data1)

data2 = pd.DataFrame([[0, 2], [1, 2]], columns=["A", "X2"])
print(data2)

data3 = pd.DataFrame([[0, 3], [1, 3]], columns=["A", "X3"])
print(data3)

data123 = reduce(
    lambda a, b: pd.merge(a, b, on="A", how="left"), 
    [data1, data2, data3]
)
print(data123)
"""
   A   X1
0  0  1.0
1  1  NaN

   A  X2
0  0   2
1  1   2

   A  X3
0  0   3
1  1   3

   A   X1  X2  X3
0  0  1.0   2   3
1  1  NaN   2   3
"""
