# -*-coding:utf-8-*-
# @auth ivann
# @time 2020-01-04
# @goal Test

from sklearn.datasets import fetch_20newsgroups

data = fetch_20newsgroups()
X, Y = data.data, data.target
