# -*-coding:utf-8-*-
# @auth ivan
# @time 20190926 18:07
# @goal test the pandas for data group by
import pandas as pd
data = pd.DataFrame([
    ["A","k1",1,2],
    ["A","k1",1,2],
    ["A","k2",1,5],
    ["B","k1",2,6],
    ["B","k1",3,6],
    ["C","k3",4,5],
    ["D","k4",4,4],
], columns=["l1","l2","l3","l4"])
print("---1---\n", data)

d1 = data.groupby(["l1", "l2"])[["l3", "l4"]].sum()
d1["l3/l4"] = d1["l3"]/d1["l4"]
print("---2---\n",d1)

d1 = data.groupby(["l1", "l2"])
print("---3---\n")
for i, j in d1:
    print(i, j)

