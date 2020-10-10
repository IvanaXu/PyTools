# -*-coding:utf-8-*-
# @auth ivan
# @time 20200611
# @goal test 054.Test_Feature_selection

from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest, f_classif
X = [[100, 1, 2, 3], [100, 4, 5, 6], [100, 7, 8, 9], [101, 11, 12, 13]]
selector = VarianceThreshold(1)
selector.fit(X)
print('Variances is %s' % selector.variances_)
print('After transform is \n%s' % selector.transform(X))
print('The surport is %s' % selector.get_support(True))
print('The surport is %s' % selector.get_support(False))
print('After reverse transform is \n%s' % selector.inverse_transform(
    selector.transform(X)))
# Variances is [ 0.1875 13.6875 13.6875 13.6875]
# After transform is
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [11 12 13]]
# The surport is [1 2 3]
# The surport is [False  True  True  True]
# After reverse transform is
# [[ 0  1  2  3]
#  [ 0  4  5  6]
#  [ 0  7  8  9]
#  [ 0 11 12 13]]

X = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [3, 3, 3, 3, 3], [1, 1, 1, 1, 1]]
y = [0, 1, 0, 1]
print('before transform:\n', X)
selector = SelectKBest(score_func=f_classif, k=3)
selector.fit(X, y)
print('scores_:\n', selector.scores_)
print('pvalues_:', selector.pvalues_)
print('selected index:', selector.get_support(True))
print('after transform:\n', selector.transform(X))
# before transform:
#  [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [3, 3, 3, 3, 3], [1, 1, 1, 1, 1]]
# scores_:
#  [0.2 0.  1.  8.  9. ]
# pvalues_: [0.69848866 1.         0.42264973 0.10557281 0.09546597]
# selected index: [2 3 4]
# after transform:
#  [[3 4 5]
#  [3 2 1]
#  [3 3 3]
#  [1 1 1]]
