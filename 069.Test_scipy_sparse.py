"""
稀疏矩阵库scipy.sparse
https://blog.csdn.net/pipisorry/article/details/41762945
http://www.bu.edu/pasi/files/2011/01/NathanBell1-10-1000.pdf
"""

import random
import numpy as np
import pandas as pd
from sklearn import metrics
from scipy import sparse as sp
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

# 文本数据 data(100*1000)为变量，但1000大多缺失; target(100*2)为目标与概率，不缺失;
data = [[
    np.nan if random.random() > 0.01 else str(random.randint(0, 10))
    for _2 in range(1000)
] for _1 in range(100)]
data = pd.DataFrame(data)
data.to_csv("069.Test_scipy_sparseX.csv", index=None, header=None)
# print(data)

target = pd.DataFrame([round(random.random(), 4) for _1 in range(100)])
target[1] = target[0].apply(lambda x: 1 if x < 0.618 else 0)
target.to_csv("069.Test_scipy_sparseY.csv", index=None, header=None)

# 读取数据
mat = sp.lil_matrix((99999, 99999))
with open("069.Test_scipy_sparseX.csv", "r") as f:
    for n, i in enumerate(f):
        for _i in i.strip("\n").split(","):
            if _i:
                mat.data[n].append(_i)
corpus = [" ".join(_) for _ in mat.data if _]
print(corpus)

_ = pd.read_csv("069.Test_scipy_sparseY.csv", header=None)
Y = _[1].tolist()
P = _[0].tolist()

# TF-IDF
tfidf = TfidfVectorizer(sublinear_tf=True, min_df=2, max_df=0.95)
tfidf.fit(corpus)
X = tfidf.transform(corpus)
# 返回即稀疏矩阵
print(X)

# 构建模型
model1 = LogisticRegression()
model1.fit(X, Y)
print(metrics.f1_score(Y, model1.predict(X)))

model2 = LogisticRegression()
_X = sp.hstack((X, sp.csr_matrix(np.array(P)).T))
model2.fit(_X, Y)
print(metrics.f1_score(Y, model2.predict(_X)))
