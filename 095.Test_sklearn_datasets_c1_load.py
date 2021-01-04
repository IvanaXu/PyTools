# -*-coding:utf-8-*-
# @auth ivann
# @time 2020-01-04
# @goal Test

from sklearn.metrics import f1_score
from sklearn.datasets import load_iris
from sklearn.tree.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = load_iris()
X, Y = data.data[:100], data.target[:100]

trai_x, test_x, trai_y, test_y = train_test_split(X, Y, train_size=0.8)

#
clf = DecisionTreeClassifier()
model = clf.fit(trai_x, trai_y)

trai_yp = model.predict(trai_x)
test_yp = model.predict(test_x)
print(
    model,
    "F1, Trai:%.6f, Test:%.6f" % 
    (f1_score(trai_y, trai_yp), f1_score(test_y, test_yp))
)

# 
clf = LogisticRegression()
model = clf.fit(trai_x, trai_y)

trai_yp = model.predict(trai_x)
test_yp = model.predict(test_x)
print(
    model,
    "F1, Trai:%.6f, Test:%.6f" % 
    (f1_score(trai_y, trai_yp), f1_score(test_y, test_yp))
)
