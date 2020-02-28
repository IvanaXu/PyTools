# -*- coding:utf-8 -*-
# @auth ivan
# @time 2020-02-28 10:14:00
# @goal test

import os
import time
import numpy as np
import pandas as pd

data = pd.DataFrame(np.random.standard_normal(10000))

t1 = "045.HDF5_FILE_t1.h5"
t2 = "045.HDF5_FILE_t2.h5"
# Notice format='table'

with pd.HDFStore(t1, 'w') as f:
    f.put(key='data', value=data, format='table')

with pd.HDFStore(t2, 'w', complevel=4, complib='blosc') as f:
    f.put(key='data', value=data, format='table')

print(data)
print(f"T1:{os.path.getsize(t1)}, T2:{os.path.getsize(t2)}, {os.path.getsize(t2)/os.path.getsize(t1)}")

time0 = time.time()
pd.read_hdf(t1, key="data")
time1 = time.time()
print(time1-time0)

time0 = time.time()
pd.read_hdf(t2, key="data")
time1 = time.time()
print(time1-time0)
"""
T1:219114, T2:104400, 0.4764643062515403
0.010165929794311523
0.009585857391357422
"""


