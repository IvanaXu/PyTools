# -*-coding:utf-8-*-
# @auth ivan
# @time 2019-09-26 18:07
# @goal test the pandas for data group by
import pandas as pd
import numpy as np

data = pd.DataFrame([
    ["A", "k1", 1, 2],
    ["A", "k1", 1, 2],
    ["A", "k2", 1, 5],
    ["B", "k1", 2, 6],
    ["B", "k1", 3, 6],
    ["C", "k3", 4, 5],
    ["D", "k4", 4, 4],
],
                    columns=["l1", "l2", "l3", "l4"])
print("---1---\n", data)

d1 = data.groupby(["l1", "l2"])[["l3", "l4"]].sum()
d1["l3/l4"] = d1["l3"] / d1["l4"]
print("---2---\n", d1)

d1 = data.groupby(["l1", "l2"])
print("---3---\n")
for i, j in d1:
    print(i, j)
"""
---1---
   l1  l2  l3  l4
0  A  k1   1   2
1  A  k1   1   2
2  A  k2   1   5
3  B  k1   2   6
4  B  k1   3   6
5  C  k3   4   5
6  D  k4   4   4
---2---
        l3  l4     l3/l4
l1 l2                  
A  k1   2   4  0.500000
   k2   1   5  0.200000
B  k1   5  12  0.416667
C  k3   4   5  0.800000
D  k4   4   4  1.000000
---3---

('A', 'k1')   l1  l2  l3  l4
0  A  k1   1   2
1  A  k1   1   2
('A', 'k2')   l1  l2  l3  l4
2  A  k2   1   5
('B', 'k1')   l1  l2  l3  l4
3  B  k1   2   6
4  B  k1   3   6
('C', 'k3')   l1  l2  l3  l4
5  C  k3   4   5
('D', 'k4')   l1  l2  l3  l4
6  D  k4   4   4
"""

df4 = pd.DataFrame([["/", 2, 3], ["", 3, 3]], columns=["A", "B", "C"])
df5 = pd.DataFrame([[1, 2, 3], [2, 3, 3]], columns=["A", "B", "C"])
df4["A"] = df4["A"].apply(lambda x: np.nan if x == "/" else "/")
df4["At"] = df4["A"].apply(lambda x: 1 if pd.isna(x) else 0)

print("---4---\n")
print(df4, "\n", df5, "\n", df4[df4["At"] == 0])

try:
    pd.merge(df4, df5, on="A")
except Exception as e:
    print(e)
# You are trying to merge on object and int64 columns. If you wish to proceed you should use pd.concat

try:
    pd.merge(df4[df4["At"] == 1], df5, on="A")
except Exception as e:
    print(e)
# You are trying to merge on object and int64 columns. If you wish to proceed you should use pd.concat

try:
    pd.merge(df4[df4["At"] == 0], df5, on="A")
except Exception as e:
    print(e)
# You are trying to merge on object and int64 columns. If you wish to proceed you should use pd.concat
