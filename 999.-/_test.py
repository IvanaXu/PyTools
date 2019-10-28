# -*-coding:utf-8-*-
# @auth ivan
# @time 2017年5月12日21:24:33
# @goal JUST FOR TEST

"""
# TEST 2017年5月10日20:06:14

import pandas
from pandas import DataFrame
paths = 'G:\\OUT\\05.个人分析目录\\sas88\\SAS\\Pro_MCC\\'
read = pandas.read_csv(paths + 'MCC_0420_t.csv', encoding='gbk')

# row = next(read.iterrows())[1]
# print(row)

# n = 0
# for i in read.itertuples():
#     print(i)
#     if n > 1000:
#         break
#     n += 1

# from numpy.random import randn
# from pandas import DataFrame
# df = DataFrame(randn(10, 2), columns=list('ab'))
# df.query('a > b')
# df[df.a > df.b]

for i in read.memory_usage():
    if i != 1592:
        print(i)

read1 = read.query("BILL > 0")
print(read1)

read2 = read.sort(['DES_LINE1'], ascending=[1])
print(read2)

read3 = read.groupby('DES_LINE1')
name = []
num = []
for i, j in read3:
    name.append(i)
    num.append(j.size)

read4 = DataFrame({'NAME': name, 'NUM': num})
print(read4)

read5 = read4.sort(['NUM'], ascending=[0])
print(read5)

# RESULT NORMAL
"""

"""
# TEST 2017年5月12日21:46:25

import utils
from load_data import Load

L = Load(utils.data_T)
print(L.dataY)
L.tPatterns()

# RESULT NORMAL
"""

"""
# TEST 2017年5月19日08:08:07
import pandas as pd
series = pd.Series([20, 21, 12, None], index=['London', 'New York', 'Helsinki', 'a'])
print(series)
print(series.describe())
print(series.set_value('London', None))
print(series.dropna(how='all'))
print(series.dropna(how='all').describe())
# RESULT NORMAL
"""
"""
# TEST AGAIN
# ADD THE DF

import pandas as pd
series_a = pd.Series([20, 21, 12, ''], index=['London', 'New York', 'Helsinki', 'a'])
series = pd.Series(series_a)

print('+__________________________________________')
print(series)
print('+__________________________________________')
print(series.describe())
print('+__________________________________________')
print(series.set_value('London', 8))
print('+__________________________________________')
print(series.dropna(how='all'))
print('+__________________________________________')
print(series.dropna(how='all').describe())
print('+__________________________________________')
# +__________________________________________
# London      20
# New York    21
# Helsinki    12
# a
# dtype: object
# +__________________________________________
# count      4
# unique     4
# top       12
# freq       1
# dtype: int64
# +__________________________________________
"""
"""
# TEST 2017年5月19日20:43:58
import pandas as pd
import numpy as np
series_a = pd.Series([20, 21, 12, np.nan])
# series_a = pd.Series([20, 21, 12, np.nan], index=['London', 'New York', 'Helsinki', 'a'])
series = pd.Series(series_a)

print('+__________________________________________')
print(series)
print('+__________________________________________')
print(series.describe())
print('+__________________________________________')
print(series.set_value('3', 8))
print(series.set_value('3', np.nan))
# 结果 当index 未申明的时候
# +__________________________________________
# 0    20.0
# 1    21.0
# 2    12.0
# 3     NaN
# 3     8.0
# dtype: float64
print('+__________________________________________')
print(series.dropna(how='all'))
print('+__________________________________________')
print(series.dropna(how='all').describe())
print('+__________________________________________')
# FIND_ED
R_POS_CNT_16_Pct_Avg_POS_CNT_1N

    # 在这里 应该是没有 -99000792.0的 TODO:上面的set没有修改到 变成重新创造了的

    # 查看影响程度(发现对原dataX的修改) 修改为定义性赋值

    # print(Categorical(dataX[i]).describe())

"""
# TODO: 没有定义index
"""
# TEST 2017-5-19 22:40:58
def a1(*args):
    print(args[0])

a1(1, 3)


def a2(**kwargs):
    if 'hi' in kwargs:
        print(kwargs['hi'])
    else:
        print(1)

a2()


def a3(a, *args):
    print(a, args[0])

a3(1, 3)
# RESULT NORMAL
"""
"""
# 代码保存

    elif fields[i] == -1:
        # 数值类型 有特殊值
        i_value = deletions[i]
        i_data = pd.DataFrame(dataX[i])
        i_data1 = pd.DataFrame(dataX[i])
        result = pd.Series()

        # for j in i_value:
        #     i_data1 = i_data1[i_data1[i] != j]
        # result = i_data1.describe()[i]
        #
        # for j in i_value:
        #     i_data2 = i_data[i_data[i] == j]
        #     s = pd.Series([i_data2[i].count()], index=['C('+str(j)+')'])
        #     result = result.append(s)

        for j in i_value:
            i_data1 = i_data1[i_data1[i] != j]

            i_data2 = i_data[i_data[i] == j]
            s = pd.Series([i_data2[i].count()], index=['C('+str(j)+')'])
            result = result.append(s)
        result = result.append(i_data1.describe()[i])
        print(result)

# 代码保存
"""

"""
In[37]: a = np.nan
In[38]: b = np.nan
In[39]: id(a)
Out[39]: 67232104
In[40]: id(b)
Out[40]: 67232104
In[41]: a == b
Out[41]: False
In[42]: a is b
Out[42]: True
In[43]: 'a' == 'a'
Out[43]: True
In[44]: 'a' is 'a'
Out[44]: True
In[45]: 1.2 == 1.2
Out[45]: True
In[46]: 1.2 is 1.2
Out[46]: True
In[47]: a = pd.Series([1,np.nan])
In[48]: for i in a:
...         print(i, i is np.nan)
...
1.0 False
nan False
In[49]: a
Out[49]:
0    1.0
1    NaN
dtype: float64
In[50]: a[1]
Out[50]: nan
In[51]: a[1] is np.nan
Out[51]: False
In[52]: a[1] is np.NaN
Out[52]: False
In[53]: b = np.nan
In[54]: b is np.nan
Out[54]: True
In[55]: a = [1, np.nan]
In[56]: for i in a""
  File "<ipython-input-56-30e2b80f5e08>", line 1
    for i in a""
               ^
SyntaxError: invalid syntax In[57]: for i in a:
...         print(i)
...
1
nan
In[58]: for i in a:
...         print(i, i is np.nan)
...
1 False
nan True

"""
"""
# np.nan 携带
import numpy as np
import pandas as pd
a = pd.Series([1, np.nan])
print(a)
for i in a:
    print(i)
    print(i == np.nan)
"""
"""
run_all = dataX.describe()



    elif fields[i] == 1:
        # 数值类型 无特殊值
        # 速度竞争
        result = run_all[i]
        # 0.09300541877746582
        # result = dataX[i].describe()
        # 1.1200640201568604
        # print(result)
"""

"""

# 保存方法 遍历处理 将特殊处理 逐个区分出来
# 但是速度会受一定的限制

result = pd.Series(name=i)

i_value = deletions[i]
i_data = pd.DataFrame(dataX[i])
i_data1 = pd.DataFrame(dataX[i])

for j in i_value:
    if j is np.nan:
        i_data1 = i_data1.dropna()
        i_data2 = pd.Series(i_data[i_data[i].isnull()])
        # 特殊处理 NAN 不被计数
    else:
        i_data1 = i_data1[i_data1[i] != j]
        i_data2 = i_data[i_data[i] == j][i]

    s = pd.Series([i_data2.count()], index=['C('+str(j)+')'], name=i)
    # append 前赋名 name=''
    result = result.append(s)

result = result.append(i_data1.describe()[i])
print(result)

# 保存方法 特征处理

        i_value = deletions[i]
        i_data = pd.DataFrame(dataX[i])
        i_data1 = dataX[i][dataX[i].isin(i_value) | (dataX[i].isnull())]
        result = pd.value_counts(i_data1, dropna=False)

        for j in i_value:
            i_data = i_data[i_data[i] != j]

        i_data = i_data.dropna()
        result = result.append(i_data.describe()[i])
        # append 前赋名 name=''
        print(result)

# 保存代码

"""

"""
# 考虑性能
spe = [-999,85,np.nan]
a = pd.Series([1,-999,-999,85,np.nan,85])
# pd.value_counts(a[ [each in spe for each in a] + a.isnull()],dropna=False)
pd.value_counts(a[ a.isin(spe) | (a.isnull())], dropna=False)

"""

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a = pd.DataFrame([
    [20, 21, 12, 13],
    [2, 4, 1, 12],
    [20, 21, 12, 13],
    [2, 4, 1, 12]
], columns=['1', '2', '3', '4'])
print(a.describe())
a.boxplot(return_type='axes')
# plt.savefig('C:\\Users\\sas88\\Desktop\\新建文件夹\\1.jpg')
plt.show()

"""

# TODO 箱形图
"""

import utils
from load_data import Load

import pandas as pd
import matplotlib.pyplot as plt

dataX = Load(utils.data_T).dataX
for i in dataX:
    print(i)
    try:
        pd.DataFrame(dataX[i]).boxplot(return_type='axes')
        plt.savefig(utils.out_path+'\\'+i+'.jpg')
    except Exception as e:
        print(str(e))
    break

#
"""

"""
dataX1 = dataX.iloc[:, 30:35]
print('___________________________________')
print(dataX1)
print('___________________________________')
print(dataX1.describe())
print('___________________________________')
# 归一化
print(dataX1.apply(lambda x: (x-np.min(x))/(np.max(x)-np.min(x))))
print('___________________________________')
# 标准化
print(dataX1.apply(lambda x: (x-np.mean(x))/(np.std(x))))
"""


# 取个数值类型的样
"""
dataX1 = dataX.iloc[:, 30:35]
print('___________________________________')
print(dataX1)
print('___________________________________')
print(dataX1.describe())
print('___________________________________')
# 归一化
print(dataX1.apply(lambda x: (x-np.min(x))/(np.max(x)-np.min(x))))
print('___________________________________')
# 标准化
print(dataX1.apply(lambda x: (x-np.mean(x))/(np.std(x))))
"""

# 取个字符类型的样
"""
dataX2 = dataX.iloc[:, 10:13]
print('___________________________________')
print(dataX2)
print('___________________________________')
for i in dataX2:
    print(pd.value_counts(dataX2[i]))
print('___________________________________')
print(pd.get_dummies(dataX2))
"""

"""
data1 = pd.DataFrame()
for i in fields:
    if not fields[i]:
        print(i)
        data = dataX[i]
        # 字符型存在缺失值 取_nan作为一列
        data_t = pd.get_dummies(data, dummy_na=True)
        for j in data_t:
            a = data_t[j].rename(str(i)+'_'+str(j))
            # data1 = data1.merge(pd.DataFrame(a), on=i)
            # print(a)
        # break
# print(data1)
"""

"""
# n = []
# for i in fields_strA:
#     print(i)
#     a = pd.get_dummies(dataX6[i], dummy_na=True)
#     print(a)
#     n.append(a)
#
# for i in n[0]:
#     for j in n[1]:
#         print('________________________')
#         print(i, j)
#         print(n[0][i] * n[1][j])
#         print('')
#
"""

"""

# print(pd.Series(dataR6).loc[:, ['R_GENDER_F', 'R_GENDER_M', 'R_GENDER_nan']])
# TODO: FIND THE ERROR
# ValueError: cannot copy sequence with size 26 to array axis with dimension 199

"""

"""
# TEST 2017年5月23日08:10:09
# a = ['A', 'B', 'C']
# print(a)
# b = {}

# a1 = dataR6['R_PRODUCT_公务卡']
# a2 = dataR6[['R_GENDER_F', 'R_GENDER_M', 'R_GENDER_nan']]
#
# for k in a2:
#     name_n = str(a1.name)+'_'+str(a2[k].name)
#     print(pd.Series(a1 * a2[k], name=name_n))
# RESULT NORMAL
"""
"""
# 删除del_
# import pandas as pd
# a = pd.DataFrame(
#     {
#         1: [1, 3, 4, 5, 6],
#         2: [1, 1, 4, 5, 6],
#         3: [1, 3, 1, 5, 6],
#         4: [1, 3, 4, 1, 6],
#         5: [1, 3, 4, 5, 1]
#      }
# )
# print(a)
#
# # del a[1, 2]
# # print(a)
#
# a = a.drop([1, 2], axis=1)
# print(a)
"""

"""

classifiers = {
    'NB': naive_bayes_classifier,
    'KNN': knn_classifier,
    'LR': logistic_regression_classifier,
    'RF': random_forest_classifier,
    'DT': decision_tree_classifier,
    # 'SVM': svm_classifier,
    # 'SVMCV': svm_cross_validation,
    'GBDT': gradient_boosting_classifier
}

is_binary_class = (len(np.unique(y_train)) == 2)
best_model = None
best_accuracy = 0
best_classifier = ''

for classifier in classifiers:
    try:
        print('******************* %s ********************' % classifier)
        start_time = time.time()
        model = classifiers[classifier](X_train, y_train)
        print('training took %fs!' % (time.time() - start_time))
        predict = model.predict(X_test)
        # if is_binary_class:
        #     precision = metrics.precision_score(y_test, predict)
        #     recall = metrics.recall_score(y_test, predict)
        #     print('precision: %.2f%%, recall: %.2f%%' % (100 * precision, 100 * recall))

        accuracy = metrics.accuracy_score(y_test, predict)
        print('accuracy: %.2f%%' % (100 * accuracy))

        if accuracy > best_accuracy:
            best_classifier = classifier
            best_model = model
            best_accuracy = accuracy
    except Exception as e:
        print(e.args)
print('******************* %s ********************' % 'END!')
print('best_classifier', best_classifier)
print('best_accuracy: %.2f%%' % (100 * best_accuracy))
print('best_model', best_model)
print('******************* %s ********************' % 'SAVE')
joblib.dump(best_model, utils.mkdir(path) + '\\best_model.model')

"""
"""
#
# from gevent import monkey
# monkey.patch_all()
# import gevent
# import time
# import random
#
#
# def sleep(i, sleeptime):
#     sleeptimes = 0
#
#     sleeptimes = sleeptimes + sleeptime
#     time.sleep(sleeptime)
#
#     sleeptime1 = random.randint(sleeptime, 2)
#     sleeptimes = sleeptimes + sleeptime1
#     time.sleep(sleeptime)
#
#     sleeptime2 = random.uniform(sleeptime1, 2)
#     sleeptimes = sleeptimes + sleeptime2
#
#     time.sleep(sleeptimes)
#     print(i, sleeptimes)
#
# time0 = time.time()
#
# for j in range(1):
#     spawnlist = []
#     for i in range(999):
#         sleeptime = random.randint(1, 2)
#         spawnlist.append(gevent.spawn(sleep, i, sleeptime))
#     gevent.joinall(spawnlist)
#     print('%d Task%d Time = %f' % (i+1, j+1, time.time() - time0))
#
"""
"""
def run(classifier):
    name = classifier.__name__
    try:
        print('******************* %s ********************' % name)
        start_time = time.time()
        model = classifier(X_train, y_train)
        print('%s Training took %fs!' % (name, time.time() - start_time))

        start_time = time.time()
        predict = model.predict(X_test)
        accuracy = metrics.accuracy_score(y_test, predict)
        print('%s Accuracy: %.2f%%' % (name, 100 * accuracy))
        print('%s Testing took %fs!' % (name, time.time() - start_time))

        if accuracy > best['best_accuracy']:
            best.update({'best_classifier': name})
            best.update({'best_model': model})
            best.update({'best_accuracy': accuracy})

    except Exception as e:
        print(e.args)

spawnlist = []
for j in range(0, 1):
    for i in classifiers:
        spawnlist.append(gevent.spawn(run, i))
gevent.joinall(spawnlist)

性能改良 不要让整体性能受最优值记录的影响

"""
# import numpy as np
#
#
# def generate_clustered_data(seed=0, n_clusters=3, n_features=2,
#                             n_samples_per_cluster=20, std=.4):
#     prng = np.random.RandomState(seed)
#
#     # the data is voluntary shifted away from zero to check clustering
#     # algorithm robustness with regards to non centered data
#     means = np.array([[1, 1, 1, 0],
#                       [-1, -1, 0, 1],
#                       [1, -1, 1, 1],
#                       [-1, 1, 1, 0],
#                      ]) + 10
#     print(means)
#
#     X = np.empty((0, n_features))
#     print(X)
#
#     for i in range(n_clusters):
#         X = np.r_[X, means[i][:n_features]
#                   + std * prng.randn(n_samples_per_cluster, n_features)]
#         print(X)
#     return X
# generate_clustered_data()

"""
Testing for Clustering methods

"""
"""
import numpy as np

from sklearn.utils.testing import assert_equal
from sklearn.utils.testing import assert_array_equal
from sklearn.utils.testing import assert_raises

from sklearn.cluster.affinity_propagation_ import AffinityPropagation
from sklearn.cluster.affinity_propagation_ import affinity_propagation
from sklearn.datasets.samples_generator import make_blobs
from sklearn.metrics import euclidean_distances

n_clusters = 3
centers = np.array([[1, 1], [-1, -1], [1, -1]]) + 10
print(centers)

X, _ = make_blobs(n_samples=60, n_features=2, centers=centers,
                  cluster_std=0.4, shuffle=True, random_state=0)
# print(X)


def test_affinity_propagation():
    # Affinity Propagation algorithm
    # Compute similarities
    S = -euclidean_distances(X, squared=True)
    print(S)

    preference = np.median(S) * 10
    print(preference)

    cluster_centers_indices, labels = affinity_propagation(
        S, preference=preference)
    print(cluster_centers_indices, labels)

    n_clusters_ = len(cluster_centers_indices)

    assert_equal(n_clusters, n_clusters_)

    af = AffinityPropagation(preference=preference, affinity="precomputed")
    labels_precomputed = af.fit(S).labels_
    print(labels_precomputed)

    af = AffinityPropagation(preference=preference, verbose=True)
    labels = af.fit(X).labels_
    print(labels)

    assert_array_equal(labels, labels_precomputed)

    cluster_centers_indices = af.cluster_centers_indices_
    print(cluster_centers_indices)

    n_clusters_ = len(cluster_centers_indices)
    assert_equal(np.unique(labels).size, n_clusters_)
    assert_equal(n_clusters, n_clusters_)

    # Test also with no copy
    _, labels_no_copy = affinity_propagation(S, preference=preference,
                                             copy=False)
    assert_array_equal(labels, labels_no_copy)

    # Test input validation
    assert_raises(ValueError, affinity_propagation, S[:, :-1])
    assert_raises(ValueError, affinity_propagation, S, damping=0)
    af = AffinityPropagation(affinity="unknown")
    assert_raises(ValueError, af.fit, X)
test_affinity_propagation()


def test_affinity_propagation_predict():
    # Test AffinityPropagation.predict
    af = AffinityPropagation(affinity="euclidean")
    labels = af.fit_predict(X)
    labels2 = af.predict(X)
    assert_array_equal(labels, labels2)


def test_affinity_propagation_predict_error():
    # Test exception in AffinityPropagation.predict
    # Not fitted.
    af = AffinityPropagation(affinity="euclidean")
    assert_raises(ValueError, af.predict, X)

    # Predict not supported when affinity="precomputed".
    S = np.dot(X, X.T)
    af = AffinityPropagation(affinity="precomputed")
    af.fit(S)
    assert_raises(ValueError, af.predict, X)
"""
#
# from scipy.stats import ks_2samp
# import pandas as pd
# ta=[0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0,
#       0, 0, 0, 0, 0, 2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
# a0=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#       0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
# a1=[2, 0, 2, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 1, 2, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0,
#       0, 0, 0, 0, 2, 2, 0, 1, 0, 0, 0, 0, 2, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0]
# a2=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#       0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
# a3=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# a4=[0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0,
#       0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
# a5=[0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0,
#       0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
# a6=[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#       0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
#
# ta = pd.Series(ta)
# a0 = pd.Series(a0)
# a1 = pd.Series(a1)
# a2 = pd.Series(a2)
# a3 = pd.Series(a3)
# a4 = pd.Series(a4)
# a5 = pd.Series(a5)
# a6 = pd.Series(a6)
#
# get_ks = lambda y1, y2: ks_2samp(y1[y2 == y1], y1[y2 != y1]).statistic
# print('a0', get_ks(ta, a0))
# print('a1', get_ks(ta, a1))
# print('a2', get_ks(ta, a2))
# print('a3', get_ks(ta, a3))
# print('a4', get_ks(ta, a4))
# print('a5', get_ks(ta, a5))
# print('a6', get_ks(ta, a6))

# from scipy import stats
# import numpy as np
# np.random.seed(12345678)
# n1 = 200
# n2 = 300
# rvs1 = stats.norm.rvs(size=n1, loc=0., scale=1)
# print(rvs1)
# rvs2 = stats.norm.rvs(size=n2, loc=0.5, scale=1.5)
# print(rvs2)
# rvs3 = stats.norm.rvs(size=n2, loc=0.01, scale=1.0)
# print(rvs3)
# rvs4 = stats.norm.rvs(size=n2, loc=0.0, scale=1.0)
# print(rvs4)
# print(stats.ks_2samp(rvs1, rvs2))
# print(stats.ks_2samp(rvs1, rvs3))
# print(stats.ks_2samp(rvs1, rvs4))
# print(ta[ta == 0].shape[0])
# print(ta[ta == 1].shape[0])
# print(ta[ta == 2].shape[0])
#
# print(a0[a0 == 0].shape[0])
# print(a0[a0 == 1].shape[0])
# print(a0[a0 == 2].shape[0])
#
# print(a0[ta == a0][a0 == 0].shape[0])
# print(a0[ta == a0][a0 == 1].shape[0])
# print(a0[ta == a0][a0 == 2].shape[0])
#

#
# def a():
#     return 1, 2
#
# b1, b2 = a()
#
# print(b1, b2)

#
# import numpy as np
# score = [0.03148661,  0.79341859,  0.82668202,  0.84745973,
#          0.86047191]
# cut0 = np.unique(
#     np.percentile(score, [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], interpolation='linear')
# )
# print('linear', cut0)
# cut0 = np.unique(
#     np.percentile(score, [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], interpolation='lower')
# )
# print('lower', cut0)
# cut0 = np.unique(
#     np.percentile(score, [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], interpolation='higher')
# )
# print('higher', cut0)
# cut0 = np.unique(
#     np.percentile(score, [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], interpolation='midpoint')
# )
# print('midpoint', cut0)
# cut0 = np.unique(
#     np.percentile(score, [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], interpolation='nearest')
# )
# print('nearest', cut0)
#
# s_max = np.max(score)
# s_min = np.min(score)
# s_t = (s_max - s_min) / 10.0
# cut1 = np.unique([s_min, s_min + s_t, s_min + 2 * s_t, s_min + 3 * s_t,
#                   s_min + 4 * s_t, s_min + 5 * s_t,
#                   s_min + 6 * s_t, s_min + 7 * s_t,
#                   s_min + 8 * s_t, s_min + 9 * s_t,
#                   s_max])
# print(cut1)

"""
# Import Library
from sklearn import svm
from sklearn.datasets import load_iris
import random
from classifier import svm_classifier

# 导入IRIS数据集
iris = load_iris()
sample_range = range(0, 150)
train_range = random.sample(sample_range, 100)
test_range = [e for e in sample_range if e not in train_range]
train_x = iris.data[train_range]
test_x = iris.data[test_range]

train_y = iris.target[train_range]
test_y = iris.target[test_range]
# print(train_y)
# print(test_y)

print('_____________________________________')
model = svm.SVC(probability=True)
model.fit(train_x, train_y)
predict = model.predict(test_x)
print(predict)
predict = model.predict_proba(test_x)
print(predict)
print('_____________________________________')
model = svm_classifier(train_x, train_y)
predict = model.predict(test_x)
print(predict)
predict = model.predict_proba(test_x)
print(predict)
print('_____________________________________')

#
# 测试结果一致,说明是数据集的问题
# 一种可能是因为占多数的类占比的比重太大了，SVM只找到了使损失函数最小化的方法
# 另一种可能是因为不平衡性并不严重，但是特征并不好，svm从你的特征之间学不到有用信息。
# 修改损失函数
#
"""
#
# from classifier import svm_classifier
# # Import Library
# from sklearn import svm
# from sklearn.datasets import load_iris
# import random
# import numpy as np
# from classifier import svm_classifier
#
# # 导入IRIS数据集
# iris = load_iris()
# sample_range = range(0, 150)
# train_range = random.sample(sample_range, 100)
# test_range = [e for e in sample_range if e not in train_range]
# train_x = iris.data[train_range]
# test_x = iris.data[test_range]
#
# train_y = iris.target[train_range]
# test_y = iris.target[test_range]
#
# print('train_y', train_y)
# for i in range(len(train_y)):
#     if train_y[i] == 2:
#         train_y.itemset(i, 0)
#     if train_y[i] == 1:
#         train_y.itemset(i, random.randint(0, 1))
# print('train_y', train_y)
# print('0%%: %.2f%%' % (train_y[train_y == 0].shape[0]/train_y.shape[0]*100))
#
# model = svm_classifier(train_x, train_y)
# predict = model.predict(test_x)
# print('predict', predict)
# predict = model.predict_proba(test_x)
# print('predict', predict)
# # 测试存在问题 不输出概率
# print('_____________________________________')

"""
from classifier import svm_classifier
# Import Library
from sklearn import svm
from sklearn.datasets import load_iris
import random
import numpy as np
from classifier import svm_classifier

# 导入IRIS数据集
iris = load_iris()
print(iris)

sample_range = range(0, 150)
train_range = random.sample(sample_range, 100)
test_range = [e for e in sample_range if e not in train_range]
train_x = iris.data[train_range]
test_x = iris.data[test_range]

train_y = iris.target[train_range]
test_y = iris.target[test_range]

for i in range(len(train_y)):
    if train_y[i] == 2:
        train_y.itemset(i, 0)
for i in range(len(test_y)):
    if test_y[i] == 2:
        test_y.itemset(i, 0)


# SVM Classifier using cross validation
def good(train_x, train_y):
    a = []
    for i in range(1, 5):
        a.append(i)

    from sklearn.grid_search import GridSearchCV
    from sklearn.ensemble import GradientBoostingClassifier
    model = GradientBoostingClassifier()
    param_grid = {'n_estimators': a}
    grid_search = GridSearchCV(model, param_grid, n_jobs=1, verbose=1)
    grid_search.fit(train_x, train_y)
    best_parameters = grid_search.best_estimator_.get_params()
    for para, val in best_parameters.items():
        print(para, val)
    model = GradientBoostingClassifier(n_estimators=best_parameters['n_estimators'])
    model.fit(train_x, train_y)
    return model

model = good(train_x, train_y)
predict = model.predict(test_x)
print('test_y', test_y)
print('predict', predict)
from sklearn import metrics
print(metrics.accuracy_score(test_y, predict))
predict_proba = model.predict_proba(test_x)
print('predict_proba', predict_proba)
print(model)

from cal import KS_Cal
result_ks, ks = KS_Cal.cal_ks(test_y, predict_proba[:, 0], draw=True)
print('KS______________________________________BEG')
print(result_ks)
print('KS值: %.2f%%' % (ks * 100))
print('KS______________________________________END')
"""

# score = [0.33148661, 0.82668202, 0.84745973, 0.86047191,
#          0.88178507, 0.89047246, 0.89916648, 0.90969703,
#          0.93082141, 0.6051739, 0.79341859]
# score.sort()
# print(score)
# index = len(score)//10
# for i in range(0, 10):
#     if i == 9:
#         print(score[i:])
#     else:
#         print(score[i:i+index])

# import pandas as pd
# a = pd.DataFrame(['a'])
# if isinstance(a, pd.DataFrame):
#     print(1)
# if type(a) == type(pd.DataFrame([])):
#     print(1)
# if type(a) == pd.core.frame.DataFrame:
#     print(1)

# import pandas as pd
# from load_data import Load
# from cal import Information_Value
# from cal import var_split as woe
# import utils
# L = Load(utils.data)
# dataX = L.dataX
# print(dataX.sort(columns='R_FQ_MTH_AMT_AVG_1N'))

# a = [1, 2, 3]
# for i in a:
#     print(i, a.index(i))

# import pandas as pd
# a = pd.DataFrame([3, 1, 2, 3], index=['4a', '1a', '2b', '3c'])
# print(a)
# a.sort_index()
# print(a)


# class A:
#     def __init__(self):
#         print('begin')
#         self.a1()
#         self.a2()
#         self.a3()
#
#     def a1(self):
#         print('a1')
#         print('a1')
#
#     def a2(self):
#         print('a2')
#
#     def a3(self):
#         print('a3')
#
#
# # a = A()
#
#
# class B(A):
#     def __init__(self):
#         super(B, self).__init__()
#
#     def a2(self):
#         print('a2')
#         print('a2')
# # b = B()
#
#
# class C(A):
#     def __init__(self):
#         super(C, self).__init__()
#
#     def a3(self):
#         print('a3')
#         print('a3')
# # c = C()
#
#
# class D(B, C):
#     def __init__(self):
#         super(D, self).__init__()
# # d = D()
#
#
# class E(A):
#     def __init__(self):
#         super(E, self).__init__()
#         self.x = 1
#
#     def a2(self):
#         print('a2')
#         print('a2')
#         self.x = 2
#
#     def a3(self):
#         print('a3')
#         print('a3')
#         self.x = 3
#
# e = E()
# print(e.x)
# e.a2()
# print(e.x)

"""

# -*-coding:utf-8-*-
# @auth LYY ivan
# @time 2017年6月9日08:24:02
# @goal tPatterns var_split

# 所有变量分段
import pandas as pd
import numpy as np
from sklearn import tree


def var_split(X, y, spe=[], min_portion=0.05):
    column_names = X.keys()
    X = X._values
    y = y._values

    splited_result = pd.DataFrame()
    for var_k in range(0, len(column_names)):
        result_each = single_var_split(X=X, y=y, var_k=var_k, column_names=column_names,
                                       min_portion=min_portion, spe=spe)

        splited_result = pd.concat([splited_result, result_each])

    return splited_result


# 但变量分段
def single_var_split(X, y, var_k, column_names, min_portion, spe):
    # 先做分段汇总, 再计算各段坏账率，IV,WOE

    x_temp = pd.Series(X.T[var_k])
    ord_spe = x_temp.isnull() | x_temp.isin(spe)

    x_spe = x_temp[ord_spe]
    x_normal = np.array(x_temp[-ord_spe])

    y = pd.Series(y)
    y_spe = y[ord_spe]
    y_normal = y[-ord_spe]

    # cross_table
    # result = pd.concat([cross_table(x=x_normal, y=y_normal, min_portion=min_portion),
    #                     pd.crosstab(x_spe, y_spe)])

    result = cross_table(x=x_normal, y=y_normal, min_portion=min_portion)
    print(result)
    # print('______________________________________________')
    result = pd.concat([result, pd.crosstab(x_spe, y_spe)])

    name0 = np.sort(result.keys())[0]
    name1 = np.sort(result.keys())[1]

    if sum((result[name0] + result[name1] == 0)) >= 1:
        zero_split = result.index[(result[name0] + result[name1] == 0)]
        result = result.drop(labels=zero_split[0], axis=0)

    Good_Self_Rate = result[name0]/np.sum(result)[name0]
    Bad_Self_Rate = result[name1]/np.sum(result)[name1]

    result['Name'] = column_names[var_k]
    result['index'] = result.index
    result['Amount'] = result[name0] + result[name1]
    result['Good_cumsum'] = np.cumsum(Good_Self_Rate)
    result['Bad_cumsum'] = np.cumsum(Bad_Self_Rate)
    result['Good_Rate'] = result[name0]/result['Amount']
    result['Bad_Rate'] = result[name1]/result['Amount']
    result['WOE'] = [-np.inf if each == 0 else np.log(each)
                     for each in Good_Self_Rate/Bad_Self_Rate]
    result['IV'] = (Good_Self_Rate - Bad_Self_Rate)*result['WOE']

    result.rename(columns={name0: 'Good', name1: 'Bad'}, inplace=True)
    result = result[['Name', 'index', 'Amount', 'Good', 'Bad', 'Good_Rate', 'Bad_Rate',
                     'Good_cumsum', 'Bad_cumsum', 'WOE', 'IV']]
    return result


# 单变量, crosstable
def cross_table(x, y, min_portion):
    x1 = np.mat(x).T

    tree_clf = tree.DecisionTreeClassifier(criterion='entropy',
                                           max_leaf_nodes=5,
                                           # min_samples_split=round(3*min_portion*len(y)),
                                           # min_samples_leaf=round(min_portion*len(y)),
                                           class_weight='balanced')

    tree_fit = tree_clf.fit(X=x1, y=y)
    cuts = np.unique(np.r_[tree_fit.tree_.threshold, [min(x), max(x)]])
    cuts = cuts[cuts >= min(x)]
    cuts.sort()
    split_x = np.array(pd.cut(x, bins=cuts, include_lowest=True))
    r = pd.crosstab(split_x, y)

    # print('+++++++')
    # print('r', r)
    # print('_______')
    s = {}
    for i in r.index:
        f = float(i.strip('[]()').split(',')[0])
        s.update({i: f})
    a = list(s.values())
    a.sort()
    # print('a', a)

    b = {}
    for i in s:
        # TODO: ValueError: '1' is not in list  b/s 重合

        b.update({i: str(a.index(s[i]) + 1)+'.'})
    # print('s', b)

    for i in range(len(r.index)):
        r.index.values[i] = b[r.index.values[i]] + r.index.values[i]

    r = r.sort_index()
    print('_______')
    return r

"""

"""
    ____________________________________________________________________________________
"""
# # -*-coding:utf-8-*-
# # @auth patrick201(YP) ivan
# # @time 2017年6月8日18:12:29
# # @goal WOE/IV Information_Value
# """
# V1.0 Github
# V1.1 Ivan
# """
# import numpy as np
# import math
# from scipy import stats
# from sklearn.utils.multiclass import type_of_target
#
#
# class WOE:
#     def __init__(self):
#         self._WOE_MIN = -20
#         self._WOE_MAX = 20
#
#     def woe(self, X, y, event=1):
#         """
#         Calculate woe of each feature category and information value
#         :param X: 2-D numpy array explanatory features which should be discreted already
#         :param y: 1-D numpy array target variable which should be binary
#         :param event: value of binary stands for the event to predict
#         :return: numpy array of woe dictionaries, each dictionary contains woe values
#                  for categories of each feature
#                  numpy array of information value of each feature
#         """
#         self.check_target_binary(y)
#         X1 = self.feature_discretion(X)
#
#         res_woe = []
#         res_iv = []
#         for i in range(0, X1.shape[-1]):
#             x = X1[:, i]
#             woe_dict, iv1 = self.woe_single_x(x, y, event)
#             res_woe.append(woe_dict)
#             res_iv.append(iv1)
#         return np.array(res_woe), np.array(res_iv)
#
#     def woe_single_x(self, x, y, event=1):
#         """
#         calculate woe and information for a single feature
#         :param x: 1-D numpy starnds for single feature
#         :param y: 1-D numpy array target variable
#         :param event: value of binary stands for the event to predict
#         :return: dictionary contains woe values for categories of this feature
#                  information value of this feature
#         """
#         self.check_target_binary(y)
#
#         event_total, non_event_total = self.count_binary(y, event=event)
#         # print(event_total, non_event_total)
#
#         x_labels = np.unique(x)
#         # print(x_labels)
#
#         woe_dict = {}
#         iv = 0
#         for x1 in x_labels:
#             y1 = y[np.where(x == x1)[0]]
#             event_count, non_event_count = self.count_binary(y1, event=event)
#             rate_event = 1.0 * event_count / event_total
#             rate_non_event = 1.0 * non_event_count / non_event_total
#             if rate_event == 0:
#                 woe1 = self._WOE_MIN
#             elif rate_non_event == 0:
#                 woe1 = self._WOE_MAX
#             else:
#                 woe1 = math.log(rate_event / rate_non_event)
#             woe_dict[x1] = woe1
#             iv += (rate_event - rate_non_event) * woe1
#         return woe_dict, iv
#
#     def woe_replace(self, X, woe_arr):
#         """
#         replace the explanatory feature categories with its woe value
#         :param X: 2-D numpy array explanatory features which should be discreted already
#         :param woe_arr: numpy array of woe dictionaries, each dictionary contains
#                woe values for categories of each feature
#         :return: the new numpy array in which woe values filled
#         """
#         if X.shape[-1] != woe_arr.shape[-1]:
#             raise ValueError('WOE dict array length must be equal with features length')
#
#         res = np.copy(X).astype(float)
#         idx = 0
#         for woe_dict in woe_arr:
#             for k in woe_dict.keys():
#                 woe = woe_dict[k]
#                 res[:, idx][np.where(res[:, idx] == k)[0]] = woe * 1.0
#             idx += 1
#
#         return res
#
#     def combined_iv(self, X, y, masks, event=1):
#         """
#         calcute the information vlaue of combination features
#         :param X: 2-D numpy array explanatory features which should be discreted already
#         :param y: 1-D numpy array target variable
#         :param masks: 1-D numpy array of masks stands for which features
#                are included in combination,
#                e.g. np.array([0,0,1,1,1,0,0,0,0,0,1]), the length should be same as features length
#         :param event: value of binary stands for the event to predict
#         :return: woe dictionary and information value of combined features
#         """
#         if masks.shape[-1] != X.shape[-1]:
#             raise ValueError('Masks array length must be equal with features length')
#
#         x = X[:, np.where(masks == 1)[0]]
#         tmp = []
#         for i in range(x.shape[0]):
#             tmp.append(self.combine(x[i, :]))
#
#         dumy = np.array(tmp)
#         # dumy_labels = np.unique(dumy)
#         woe, iv = self.woe_single_x(dumy, y, event)
#         return woe, iv
#
#     def combine(self, list):
#         res = ''
#         for item in list:
#             res += str(item)
#         return res
#
#     def count_binary(self, a, event=1):
#         event_count = (a == event).sum()
#         non_event_count = a.shape[-1] - event_count
#         return event_count, non_event_count
#
#     def check_target_binary(self, y):
#         """
#         check if the target variable is binary, raise error if not.
#         :param y:
#         :return:
#         """
#         y_type = type_of_target(y)
#         if y_type not in ['binary']:
#             raise ValueError('Label type must be binary')
#
#     def feature_discretion(self, X):
#         """
#         Discrete the continuous features of input data X,
#         and keep other features unchanged.
#         :param X : numpy array
#         :return: the numpy array in which all continuous features are discreted
#         """
#         temp = []
#         for i in range(0, X.shape[-1]):
#             x = X[:, i]
#             x_type = type_of_target(x)
#
#             if x_type == 'continuous':
#                 x1 = self.discrete(x)
#                 temp.append(x1)
#             else:
#                 temp.append(x)
#         return np.array(temp).T
#
#     def discrete(self, x):
#         """
#         Discrete the input 1-D numpy array using 5 equal percentiles
#         :param x: 1-D numpy array
#         :return: discreted 1-D numpy array
#         """
#         res = np.array([0] * x.shape[-1], dtype=int)
#         for i in range(5):
#             point1 = stats.scoreatpercentile(x, i * 20)
#             point2 = stats.scoreatpercentile(x, (i + 1) * 20)
#             x1 = x[np.where((x >= point1) & (x <= point2))]
#             mask = np.in1d(x, x1)
#             res[mask] = (i + 1)
#         return res
#
#     @property
#     def WOE_MIN(self):
#         return self._WOE_MIN
#
#     @WOE_MIN.setter
#     def WOE_MIN(self, woe_min):
#         self._WOE_MIN = woe_min
#
#     @property
#     def WOE_MAX(self):
#         return self._WOE_MAX
#
#     @WOE_MAX.setter
#     def WOE_MAX(self, woe_max):
#         self._WOE_MAX = woe_max
#
"""
    ____________________________________________________________________________________
"""
# w = Information_Value.WOE()
# for i in dataX.columns:
#     print(i)
#     try:
#         woe, iv = w.woe_single_x(np.array(dataX[i]), np.array(dataY))
#         print('woe', woe)
#         for i in woe:
#             print(i, woe[i])
#         print('iv', iv)
#     except Exception as e:
#         print(e.args)
#
#     break
# print(type(pd.DataFrame(dataY)))
# print(type(pd.DataFrame(dataX)))

# for i in dataX.columns:
#     print(i)
#     # print(dataX[i])
#
#     try:
#         var_split.var_split(dataX[i], dataY)
#     except Exception as e:
#         print(e.args)

# TODO:
# log = u'G:\\OUT\\07.AI\\MachineLearning\\out\\20170612\\out1000.log'
#
#
# def ap(string):
#     print(string)
#     with open(log, 'a+', encoding='utf-8') as f:
#         f.write(string + '\n')
#
# for i in dataX.keys():
#     print(i)
#     try:
#         ar = woe.var_split(dataX[[i]], dataY, spe=[-99000792, -99000784, -99000776])
#         for j in ar:
#             ap(j)
#             for k in ar[j]:
#                 ap(str(k))
#     except Exception as e:
#         ap('__________ERROR_________')
#         ap(str(e.args))
#         ap('__________ERROR_________')
#     # break

# import numpy as np
# print(-np.inf)

# # 重置索引
# x_temp = pd.Series(x.T[var_k])
#
# ord_special = x_temp.isnull() | x_temp.isin(spe)
# x_special = x_temp[ord_special]
# x_normal = np.array(x_temp[-ord_special])
# # x_normal = x_temp[-ord_special]
#
# # pandas.core.indexing.IndexingError: Unalignable boolean Series key provided
# # 直接取用了x_temp去null和特殊值的对位
# y_special = y[list(ord_special)]
# y_normal = y[list(-ord_special)]

"""
Test Time: 2017年6月14日08:54:20
"""
# import pandas as pd
# a = pd.DataFrame([[1, 3, 4], [3, 6, 4]], columns=['a1', 'a2', 'a3'])
# print(a)
#    a1  a2  a3
# 0   1   3   4
# 1   3   6   4

# a['s1'] = sum(a['a1'])
# a['a1/s1'] = a['a1']/a['s1']
# a['s2'] = sum(a['a2'])
# a['a2/s2'] = a['a2']/a['s2']
# a['s3'] = sum(a['a3'])
# a['a3/s3'] = a['a3']/a['s3']
# print(a)
#    a1  a2  a3  s1  a1/s1  s2     a2/s2  s3  a3/s3
# 0   1   3   4   4   0.25   9  0.333333   8    0.5
# 1   3   6   4   4   0.75   9  0.666667   8    0.5

# print(a.sum())
# a1        4.0
# a2        9.0
# a3        8.0
# s1        8.0
# a1/s1     1.0
# s2       18.0
# a2/s2     1.0
# s3       16.0
# a3/s3     1.0
# dtype: float64

# import numpy as np
# key = np.sort(a.keys())
# # min
# name0 = key[0]
# r0 = a[name0]
# # max
# name1 = key[1]
# r1 = a[name1]
#
# print(r0, r1)
# g = r0/np.sum(a)[name0]
# b = r1/np.sum(a)[name1]
# print(g)
# print(b)
# print(g/b)
# print(np.log(0))
#
# a['WOE'] = [-np.inf if not j else np.log(j) for j in g/b]
# print(a)
"""
Alt + Shift + Up
"""
"""
Alt + Shift + E
"""
#
#
# def a(x):
#     print('a', 1)
#     b(x=2)
#     return x
#
#
# def b(x):
#     print('b', 6)
#     return x
#
# print(a(x=1))
# 测试调试工具
#
#

"""
做一些微调还是可以的
"""

#
# import numpy as np
# import pandas as pd
# from sklearn import tree
# from load_data import Load
#
# import utils
#
# L = Load(utils.data)
# dataX = L.dataX
# dataY = L.dataY
#
# # -*-coding:utf-8-*-
# # @auth LYY ivan
# # @time 2017年6月12日20:58:19
# # @goal tPatterns var_split
# """
#     1.DecisionTreeClassifier
#     2.if IV <  0.1: pass
#       if IV >= 0.1: continue
#     3.Sample 20 Times
# """
# # TODO: N = 20; MayBe Can So More;
# # TODO：取出Key值
# import pandas as pd
# import numpy as np
# from sklearn import tree
# # from cal import Draw_Tree as dt
# import utils
# N = 20
#
# i2 = ['R_FQ_MTH_AMT_AVG_1N']
# i1 = ['R_PUR_16_Pct_Avg_PUR_7N', 'R_FQ_MTH_AMT_AVG_1N', 'R_BAL_FQ_AVG_13']
# t = ['R_PRODUCT',
#      'R_GENDER',
#      'R_MAR_DES',
#      'R_EDUCA_DES',
#      'R_HOME_DES',
#      'R_AUTO_PAY_CODE']
#
#
# def var_split(x, y, spe=None, column_names=None, min_portion=0.05):
#     """
#     # 如果是pd.DataFrame格式，转换成np.array格式
#     :param x: dataX
#     :param y: dataY
#     :param column_names: []
#     :param spe: Special Value, Like [-99000792, -99000784, -99000776]
#     :param min_portion: Min Potion
#     [1, 2, 3] min_portion = 0.33 >> [1]
#     :return: split_result
#     """
#     if isinstance(x, pd.DataFrame):
#         if not column_names:
#             column_names = x.keys()
#         elif len(column_names) != len(x.columns):
#             raise Exception("'X' has {0} variables, but para 'column_names' has {1}"
#                             .format(len(x.columns), len(column_names)))
#     if not spe:
#         spe = []
#
#     split_result = pd.DataFrame([])
#     x = x.values
#
#     for i in range(len(column_names)):
#         result_each = single_var_split(x=x, y=y, var_k=i,
#                                        column_names=column_names,
#                                        min_portion=min_portion,
#                                        spe=spe)
#         split_result = pd.concat([split_result, result_each])
#
#     return split_result
#
#
# def single_var_split(x, y, var_k, column_names, min_portion, spe):
#     # TODO: column_names 不应该作为参数传进来
#     """
#     # 单变量分段, 先做分段汇总，再计算各段坏账率，IV,WOE
#     :param x: numpy.array, dataX.values
#     :param y: dataY
#     :param var_k: Key For The dataX
#     :param column_names:
#     :param min_portion:
#     :param spe:
#     :return:
#     """
#     # 重置索引
#     x_temp = pd.Series(x.T[var_k])
#
#     ord_special = x_temp.isnull() | x_temp.isin(spe)
#     x_special = x_temp[ord_special]
#     x_normal = np.array(x_temp[-ord_special])
#     # x_normal = x_temp[-ord_special]
#
#     # 直接取用了x_temp去null和特殊值的对位
#     y_special = y[list(ord_special)]
#     y_normal = y[list(-ord_special)]
#
#     # count |0|1|, [normal] concat [special]
#     result = pd.concat([cross_table(x=x_normal, y=y_normal, min_portion=min_portion),
#                         pd.crosstab(x_special, y_special)])
#
#     # 整体IV值计算
#     # TODO: Change The result._name_
#
#     result_1 = iv_cal(result)
#     result_1['Name'] = column_names[var_k]
#     result_1['IV'] = sum(result_1['IVi'])
#     result_1 = result_1[['Name', 'min', 'Count', 'Good', 'Bad', 'Good_Rate', 'Bad_Rate',
#                          # 'Good_CumSum', 'Bad_CumSum',
#                          'WOE', 'IVi', 'IV']]
#     # 排序，并替代原数据集
#     result_1.sort_values(by='min', inplace=True)
#     return result_1
#
#
# def cross_table(x, y, min_portion):
#     if np.unique(x).__len__() - 1:
#         tree_clf = tree.DecisionTreeClassifier(
#             max_leaf_nodes=5,
#             min_samples_split=round(3*min_portion*len(y)),
#             min_samples_leaf=round(min_portion*len(y)),
#             class_weight='balanced')
#         tree_fit = tree_clf.fit(X=np.mat(x).T, y=y)
#
#         # draw(path=utils.out_path,
#         #      d_tree=tree_fit,
#         #      name='var_split')
#
#         cuts = np.unique(np.r_[tree_fit.tree_.threshold, [min(x), max(x)]])
#         cuts = cuts[cuts >= min(x)]
#         cuts.sort()
#
#         split_x = np.array(pd.cut(x, bins=cuts, include_lowest=True))
#
#         # 计算单调性
#         t_cross_table = pd.crosstab(split_x, y)
#         cross_table_1 = iv_cal(t_cross_table)
#
#         # 判断是否单调，且有区分能力
#         # TODO:抽离出来计算IV值和判断是否单调的部分，然后根据输入输出类型进行设定，避免复用。
#         # TODO:根据测试情况，整体循环次数至少还可以上到500次，做一次循环，判断是否单调，有效即结束。
#         # TODO:
#         if abs(cross_table_1[['min', 'Bad_Rate']].corr(method='spearman').ix[0, 1]) - 1 \
#                 and cross_table_1['IVi'].sum() >= 0.1:
#             # 抽样
#             new_cuts = monotonical(x=x, y=y, min_portion=min_portion)
#             split_x_1 = np.array(pd.cut(x, bins=new_cuts, include_lowest=True))
#             # 计算单调性
#             t_cross_table = pd.crosstab(split_x_1, y)
#             return t_cross_table
#         else:
#             return pd.crosstab(split_x, y)
#     else:
#         # 整变量仅一个值，无需进行分箱
#         return pd.crosstab(x, y)
#
#
# def iv_cal(result):
#     """
#     # 计算IV值
#     :param result: pd.crosstab(), Like Count |0|1|
#     :return: result
#     """
#     key = np.sort(result.keys())
#     # min
#     name0 = key[0]
#     r0 = result[name0]
#     # max
#     name1 = key[1]
#     r1 = result[name1]
#
#     # 若分段无数值, drop掉
#     if sum((r0 + r1 == 0)) >= 1:
#         zero_split = result.index[(r0 + r1 == 0)]
#         result = result.drop(labels=zero_split[0], axis=0)
#
#     good_self_rate = r0/np.sum(result)[name0]
#     bad_self_rate = r1/np.sum(result)[name1]
#
#     result['min'] = [float(j.strip('()[]').split(',')[0])
#                      if isinstance(j, str) else j for j in result.index]
#     result['Count'] = r0 + r1
#     # result['Good_CumSum'] = np.cumsum(good_self_rate)
#     # result['Bad_CumSum'] = np.cumsum(bad_self_rate)
#     result['Good_Rate'] = r0/(r0 + r1)
#     result['Bad_Rate'] = r1/(r0 + r1)
#     result['WOE'] = [-np.inf if not j else np.log(j)
#                      for j in good_self_rate/bad_self_rate]
#     result['IVi'] = (good_self_rate - bad_self_rate) * result['WOE']
#
#     result.rename(columns={name0: 'Good', name1: 'Bad'}, inplace=True)
#     return result
#
#
# # TODO: Need Change !
# # TODO: Need Change !
# # TODO: Need Change !
#
# def monotonical(x, y, min_portion):
#     """
#     # 抽样
#     :param x:
#     :param y:
#     :param min_portion:
#     :return:
#     """
#     max_x = max(x)
#     min_x = min(x)
#     cross_table_all = []
#     spearmans = []
#     corrs = []
#     for each_k in range(0, N):
#         data_1 = pd.DataFrame({'x': x, 'target': y})
#
#         data_1_0 = data_1.ix[data_1['target'] == 0, :]
#         data_1_1 = data_1.ix[data_1['target'] == 1, :]
#
#         # 抽样
#         data_all = pd.concat([
#             data_1_0.sample(n=min(len(data_1_0), len(data_1_1)), replace=True),
#             data_1_1.sample(n=min(len(data_1_0), len(data_1_1)), replace=True)])
#
#         # 分段
#         temp_x = data_all['x']
#         temp_y = data_all['target']
#         tree_clf = tree.DecisionTreeClassifier(
#             max_leaf_nodes=5,
#             min_samples_split=round(3 * min_portion * len(temp_y)),
#             min_samples_leaf=round(min_portion * len(temp_y)),
#             class_weight='balanced')
#         tree_fit = tree_clf.fit(X=np.mat(temp_x).T, y=temp_y)
#
#         cuts = np.unique(np.r_[tree_fit.tree_.threshold, [min(temp_x), max(temp_x)]])
#         cuts = cuts[cuts >= np.min(temp_x)]
#         cuts.sort()
#         split_x = np.array(pd.cut(temp_x, bins=cuts, include_lowest=True))
#         cross_table_temp = pd.crosstab(split_x, temp_y)
#         # cross_table_temp = cross_table(x=data_all['x'], y=data_all['target'], min_portion=min_portion)
#         name1 = max(cross_table_temp.keys())
#         cross_table_temp['Bad_Rate'] = cross_table_temp[name1] / np.sum(cross_table_temp, axis=1)
#         cross_table_temp['min'] = [float(each.strip('()[]').split(',')[0])
#                                    for each in cross_table_temp.index]
#         cross_table_temp.sort_values(by='min', inplace=True)
#         cross_table_all.append(cross_table_temp)
#         spearmans.append(abs(cross_table_temp[['min', 'Bad_Rate']].corr(method='spearman').ix[0, 1]))#秩相关，判断单调
#         corrs.append(abs(cross_table_temp[['min', 'Bad_Rate']].corr().ix[0, 1]))
#
#     # 取spearmans最大的下标，在这里面再取corrs最大的下标，return cross_table_all[k]
#     index_one = np.argwhere(spearmans == max(spearmans))
#     corrs_temp = np.array(corrs)[index_one]
#     final_index = index_one[index_one == np.argwhere(corrs == max(corrs_temp))]
#     new_cuts = list(cross_table_all[final_index[0]]['min'])
#     new_cuts.pop(0)
#     new_cuts.append(max_x)
#     new_cuts.insert(0, min_x)
#     return new_cuts
#
#
# try:
#     for i in i1:
#         print('BEGIN _________________________')
#         print(i)
#         a = var_split(dataX[[i]], dataY, spe=[-99000792, -99000784, -99000776])
#         print('_END_ _________________________')
#         print(a)
#         break
# except Exception as e:
#     print(e.args)
#
#
# import numpy as np
# a = [1, 2, 4, 8]
#
# b = [3, 2, 5, 3]
# print(a, b)
#
# a = np.array(a)
# a1 = np.argwhere(a == max(a))
# print(a1)
# b1 = np.argwhere(b == max(b))
# print(b1)
# b2 = np.argmax(b)
# print(b2)

# aa = [1, 3, 4]
# print(aa.pop(0))
# print(aa)
# aa.insert(0, 122)
# print(aa)
# import pandas as pd
# import numpy as np
# a = {
#     1: 5,
#     2: 20
# }
# print(a)
# print(max(a.values()))
#
# max_a = 0
# max_i = 0
# for i in a:
#     if a[i] > max_a:
#         max_a = a[i]
#         max_i = i
# print(max_i)
# #
# b = [a[i] if a[i] > max_a else max_a for i in a]
# print(b)
# import numpy as np
# import pandas as pd
# a = pd.DataFrame([[1, 2, 4], [2, 6, 3], [3, 10, 1]], columns=['a', 'b', 'c'])
# print(a)
#
# print(a[['a', 'b']].corr().ix[0, 1])
# a = [1, 2, 3, 4, 5]
# print(a)
# a[0] = 2
# print(a)
# import numpy as np
# import pandas as pd
# a1 = [1, 2]
# a2 = [1, 3]
# print(np.r_[a1, a2])
# a = a1 + a2
# b = np.array(a)
# b1 = np.array(a1)
# b2 = np.array(a2)
# print(b1, b2)
#
# import pandas as pd
# import datetime
#
# date = []
# # holiday = {
# #     ['0101-0102']: 2,
# #     ['0402-0404', '0429-0501', '0528-0530']: 3,
# #     ['0127-0202']: 7,
# #     ['1001-1008']: 8
# # }
#
# live_day = {
#     u'元宵节': '0211',
#     u'情人节': '0214',
#     u'妇女节': '0308',
#     u'植树节': '0312',
#     u'愚人节': '0401',
#     u'青年节': '0504',
#     u'母亲节': '0514',
#     u'儿童节': '0601',
#     u'父亲节': '0618',
#     u'七夕节': '0828',
#     u'中元节': '0905',
#     u'教师节': '0910',
#     u'重阳节': '1028',
#     u'感恩节': '1123',
#     u'冬至节': '1222',
#     u'平安夜': '1224',
#     u'圣诞节': '1225',
# }
#
#
# def get_tomorr(i):
#     now = datetime.datetime.strptime('20170101', '%Y%m%d')
#     yes = now + datetime.timedelta(hours=24*(i-1))
#     return yes.strftime('%m%d')
#
#
# def get_tomorr1(i):
#     r = i.split('-')
#     i0, i1 = r[0], r[1]
#     t = i0
#     r1 = []
#     while t <= i1:
#         r1.append(t)
#         now = datetime.datetime.strptime('2017'+t, '%Y%m%d')
#         yes = now + datetime.timedelta(hours=24)
#         t = yes.strftime('%m%d')
#     return r1
#
#
# for i in range(1, 366):
#     d1 = get_tomorr(i)
#     d2 = 0
#     d3 = 0
#     if d1 in liveday.values():
#         d3 = 1
#     print('2017'+d1+','+str(d2)+','+str(d3))
#
# import numpy as np
# import pandas as pd
# a1 = [1, 2]
# a2 = [1, 3]
# print(np.r_[a1, a2])
# print(np.r_[np.array(a1), a2])
# print(np.r_[a1, np.array(a2)])
# print(np.r_[np.array(a1), np.array(a2)])
#
# print(a1 + a2)
# print(np.array(a1 + a2))
# print(np.array(a1)+np.array(a2))

# import numpy as np
# per = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# a = np.array([10, 7, 4, 3, 2, 1, 10, 7, 4, 3, 2, 1, 10, 7, 4, 3, 2, 1])
# print(np.percentile(a, per))
#
# for i in per:
#     print(np.percentile(a, i))
# b = [1, 3]
# print(type(np.unique(b)))

# a = [1, 2, 3]
# b = [2, 1]
# # for i in b:
# #     a.remove(i)
# # print(a)
# import pandas as pd
# a1 = pd.Series(a)
# b1 = pd.Series(b)
# print(a1)
# print(b1)
# print(a1[-a1.isin(b1)])

# 优雅使用Python

# 1
# a = 1
# b = 2
# print(a, b)
# a, b = b, a
# print(a, b)

# 2 生成器
# for i in range(0, 10000000000):
#     if i == 9999999:
#         print(i)

# 3
# a = ['A', 'B', 'C', 'D']

# for i in a:
#     print(a.index(i), i)
#
# for i, j in enumerate(a):
#     print(i, j)

# 4
# a = ['A', 'B', 'C', 'D']
# print(''.join(a))
# # print('1001'.center(8, '2'))
# print('|'.join(a))

# 5
# with open('1.txt', 'r') as f:
#     f.readlines()

# 6
# result = []
# for i in range(0, 10):
#     s = i ** 2
#     result.append(s)
# print(result)
#
# # pythonic
# a = [i ** 2 for i in range(0, 10)]
# print(a)

# 7

# 8
# a = ['A', 'B', 'C', 'D']
# print(a)
#
# a1 = a.copy()
# a1.pop(0)
# a1.insert(0, '0A')
# print(a1)
#
# a2 = a.copy()
# a2[0] = '0A'
# print(a2)
#
# from collections import deque
# a3 = deque(a)
# print(a3)
# a3.popleft()
# print(a3)
# a3.appendleft('0A')
# print(a3)
# a3.pop()
# print(a3)

# 9
# p = 'A', 'B', 'C', 'D'
# a1, a2, a3, a4 = p
# print(a1, a2, a3, a4)

# # 10
# a = {}
# for i in range(0, 10000):
#     a.update({i: str(i)})
# print(a)
#
# for i in a:
#     print(i, a[i])
#
# for i, j in a.items():
#     print(i, j)

# 11
# a = 15
# if 18 > a > 10:
#     print(1)

# 12
# a = 15
# b = ''
# if a == 15:
#     b = '1'
# else:
#     b = '0'
# print(b)
#
# # b = ''
# b = '1' if a == 15 else '0'
# print(b)

# 13
# for i in range(0, 12):
#     print(i)
# else:
#     print('end!')
#
# for i in range(0, 12):
#     print(i)
#     if i == 2:
#         break
# else:
#     print('end!')

# 14
# a = 'HI'
# b = 'GOOD MORNING'
# print('%s ivan,%s!' % (a, b))
# print('{s1} ivan,{s2}!'.format(s1=a, s2=b))

# 15
# a = [1, 2, 3, 4, 5, 6, 7]
# print(a)
# print(a[1:])
# print(a[1::2])

# 16
#
#
# def fib1(n):
#     a, b = 0, 1
#     result = []
#     while b < n:
#         result.append(b)
#         a, b = b, a+b
#     return result
#
# print(fib1(10))
#
#
# def fib2(n):
#     a, b = 0, 1
#     while b < n:
#         yield b
#         a, b = b, a+b
# for i in fib2(10):
#     print(i)
#
# # def f1():
# #     for i in range(0, 5):
# #         yield i
# #
# # for i in f1():
# #     print(i)

# 17
# a = {'0': '0A', '1': '1B'}
# b1 = '0'
# b2 = '0 '
# c = 'NONE'
#
# if b1 in a:
#     print(a[b1])
# else:
#     print(c)
#
# print(a.get(b1, c))
#
# if b2 in a:
#     print(a[b2])
# else:
#     print(c)
#
# print(a.get(b2, c))

# 18
# a = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
# b = {}
# for (i, j) in a:
#     print(i, j)
#     if i in b:
#         b[i].append(j)
#     else:
#         b[i] = [j]
# print(b)
#
# c = {}
# for (i, j) in a:
#     c.setdefault(i, []).append(j)
# print(c)
#
# from collections import defaultdict
# d = defaultdict(list)
# print(d)
# for (i, j) in a:
#     d[i].append(j)
# print(d)

# 19
# a = [1, 2, 3]
#
# b = {i: i**2 for i in a}
# print(b)
#
# c = {i: i**2 for i in a if i > 1}
# print(c)
#
# # low
# # e = {}
# # for i in a:
# #     if i > 1:
# #         e.update({i: i**2})
# # print(e)
#
# f = {i: i**2 for i in a if i > 1}
# print(f)
# f1 = [i for i in a if i > 1]
# print(f1)
# #
# import pandas as pd
# import numpy as np
#
# sp = [4002, 5675]
# index = ['a1', 'b2', 'c3', 'd4', 'd5', 'd6']
#
# a = pd.DataFrame(
#     [[1, 1], [11, 0], [21, 1],
#      [4002, 0], [5675, 1], [22, 0]],
#     index=index,
#     columns=['X', 'Y'])
# b = a.to_string().split('\n')
# for i in b:
#     print(i)
#
# b = pd.DataFrame(
#     [[1, 41], [11, 3], [21, 11],
#      [4002, 80], [5675, 16], [22, 40]],
#     index=index,
#     columns=['X', 'Z'])
#
# c = pd.merge(a, b)
# # print(c[['X', 'Y']])
# print(c['Z'])


# x = a['X']
# y = a['Y']
#
# x_sp = x[x.isin(sp)]
# y_sp = y[x.isin(sp)]
# x_no = x[-x.isin(sp)]
# y_no = y[-x.isin(sp)]
#
# print('____x_sp')
# print(x_sp)
# print('____y_sp')
# print(y_sp)
# print('____x_no')
# print(x_no)
# print('____y_no')
# print(y_no)

# new_cuts = [1, 10, 20, 30]
# t_split_x = pd.DataFrame(pd.cut(x, bins=new_cuts, include_lowest=True))
# print('t_split_x', t_split_x)
# for i in x_sp.index:
#     print(i)
# for i in x_sp.values:
#     print(i)

# for i, j in x_sp.items():
#     print(type(i), i)
#     print(type(j), j)
# _______________________________________________________
# _______________________________________________________
# t_split_x.update(x_sp)
# _______________________________________________________
# _______________________________________________________
# print('t_split_x', t_split_x)
# a['X'] = t_split_x['X']
# print(a)

# x0 = pd.merge(t_split_x, pd.DataFrame(x_sp, index=x_sp.index), how='left',
#               left_index=True, right_index=True)
# print(x0)

# sp = pd.DataFrame(x_sp)
# sp['Y'] = pd.DataFrame(y_sp)
# print(sp)
#
# no = pd.DataFrame(t_split_x)
# no['Y'] = pd.DataFrame(y_no)
# print(no)
# 或者根据index

# print(x)
# new_cuts = [1, 10, 20, 30]
# t_split_x1 = {x: pd.cut(x, bins=new_cuts, include_lowest=True)}
# print(t_split_x1)

# def f(x):
#     return str(x+1) + 's'
#
# print(x.apply(f))
#

"""
new_cuts = [1, 10, 20, 30]
t_split_x = pd.DataFrame(pd.cut(x, bins=new_cuts, include_lowest=True))
print('t_split_x', t_split_x)
t_split_x.update(x_sp)
print('t_split_x', t_split_x)
a['X'] = t_split_x['X']
print(a)
"""

"""
IMPORT
"""
# import pandas as pd
# index = ['a1', 'b2', 'c3', 'd4', 'd5', 'd6']
#
# a = pd.DataFrame(
#     [[1, 1], [11, 0], [21, 1],
#      [4002, 0], [5675, 1], [22, 0]],
#     index=index,
#     columns=['X', 'Y'])
# b = pd.DataFrame(
#     [['[1, 10]', 21], ['(10, 20]', 42], ['(20, 30]', 13]],
#     columns=['X', 'WOE']
#     )
#
# print(a)
# new_cuts = [1, 10, 20, 30]
# t_split_x = pd.DataFrame(pd.cut(a['X'], bins=new_cuts, include_lowest=True))
# a.update(t_split_x)
# print(a)
# b_all = {}
# for i, j in b.values:
#     b_all.update({i: j})
# a.replace(to_replace={'X': b_all}, inplace=True)
# print(a)
#
# a = a.drop('Y', axis=1)
# print(a)


"""
"""

# import pandas as pd
# import numpy as np
# index = ['a1', 'b2', 'c3', 'd4', 'd5', 'd6']
#
# a = pd.DataFrame(
#     [[1, 1], [11, 0], [21, 1],
#      [4002, 0], [5675, 1], [22, 0]],
#     index=index,
#     columns=['X', 'Y'])
# print(a)
# new_cuts = [1, 10.5, 20, 30, 3, 1.0]
# new_cuts.sort()
# new_cuts = np.unique(new_cuts)
# t_split_x = pd.DataFrame(pd.cut(a['X'], bins=new_cuts, include_lowest=True))
# print(t_split_x)
#
# new_cuts = [1, 10.5]
# new_cuts.sort()
# new_cuts = np.unique(new_cuts)
# t_split_x = pd.DataFrame(pd.cut(a['X'], bins=new_cuts, include_lowest=True))
# print(t_split_x)

# import pandas as pd
# index = ['a1', 'b2', 'c3', 'd4', 'd5', 'd6']
# a = pd.DataFrame(
#     [
#         [-99000784, 1],
#         [-99000784, 0],
#         [-99000784, 1],
#         [-99000784, 0],
#         [-99000784, 1],
#         [-99000784, 0]
#     ],
#     index=index,
#     columns=['X', 'Y'])
# b = a[a['Y'] == 1]
# print(a)
# print(b)
#
# print()
# a1 = pd.crosstab(a['X'], a['Y'])
# print(a1)
#
# print()
# b1 = pd.crosstab(b['X'], b['Y'])
# print(b1)
#
# print()
# b2 = pd.crosstab(b['X'], b['Y'])
# print(b2)

# import pandas as pd
# import numpy as np
# a = pd.Series([1, 3, np.nan])
# print(a)
# a.fillna(0, inplace=True)
# print(a)
# import os
# cmd = 'D:\\Python35\\python.exe G://OUT//07.AI//MachineLearning//develop//MLTv2.1//classifier_run.py'
# for i in range(50):
#     print(i)
#     os.system(cmd)

# import matplotlib.pyplot as plt
# fig = plt.figure()
# global a
# print(a)

# import pandas as pd
# import utils
# a = pd.DataFrame([1,2,3])
# path = utils.out_path + '/' + utils.get_time() + '/'
# print(a)
# a.to_csv(utils.mkdir(path)+'tPatterns.csv')

