# -*-coding:utf-8-*-
# @auth ivan
# @time 20200220 17:00:00
# @goal test the hdf5

import os
import h5py
import numpy as np


def f(x, y, t):
    imgData = np.zeros((x, y))
    print(imgData.shape)

    fh5, csv = f"045.HDF5_FILE_{t}.h5", f"045.HDF5_FILE_{t}.csv"

    # HDF5的写入
    with h5py.File(fh5, 'w') as f:
        f['data'] = imgData
        f['labels'] = range(100)

    # HDF5的读取
    with h5py.File(fh5, 'r') as f:
        # print(f.keys())
        print(f['data'][:])

    np.savetxt(csv, imgData, delimiter=',')

    print(
        f"{fh5}:{os.path.getsize(fh5)}, {csv}:{os.path.getsize(csv)}, {os.path.getsize(fh5)/os.path.getsize(csv)}"
    )


f(2, 2, "little")
"""
(2, 2)
[[0. 0.]
 [0. 0.]]
045.HDF5_FILE_little.h5:2880, 045.HDF5_FILE_little.csv:100, 28.8
"""

f(200, 200, "big")
"""
(200, 200)
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
045.HDF5_FILE_big.h5:322848, 045.HDF5_FILE_big.csv:1000000, 0.322848
"""
