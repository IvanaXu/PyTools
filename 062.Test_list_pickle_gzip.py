# -*-coding:utf-8-*-
# @auth Ivan
# @time 20200820
# @goal test pickle and gzip

import gzip
import random
import pickle

# 1
with open("062.Test_list_pickle_gzip.pkl", "wb") as f:
    pickle.dump([1 if random.random() > 0.9 else 0 for _ in range(99999)], f)
# -rw-r--r--  1 ivan  staff   196K  8 20 09:38 062.Test_list_pickle_gzip.pkl
with open("062.Test_list_pickle_gzip.pkl", "rb") as f:
    data = pickle.load(f)
    print(sum(data))

# 2
with gzip.open("062.Test_list_pickle_gzip.compkl", "wb") as f:
    pickle.dump([1 if random.random() > 0.9 else 0 for _ in range(99999)], f)
# -rw-r--r--  1 ivan  staff   196K  8 20 09:38 062.Test_list_pickle_gzip.pkl
with gzip.open("062.Test_list_pickle_gzip.compkl", "rb") as f:
    data = pickle.load(f)
    print(sum(data))
# -rw-r--r--  1 ivan  staff   9.4K  8 20 09:39 062.Test_list_pickle_gzip.compkl
# -rw-r--r--  1 ivan  staff   196K  8 20 09:39 062.Test_list_pickle_gzip.pkl



