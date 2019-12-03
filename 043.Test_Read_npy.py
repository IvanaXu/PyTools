# -*-coding:utf-8-*-
# @auth ivan
# @time 20191203 181430
# @goal test the npy
import numpy as np
n = np.random.rand(3, 4, 5)
print("-"*100+"\n", n)
np.save('043.Test_Read_npy.npy', n)

n = np.load('043.Test_Read_npy.npy')
print("-"*100+"\n", n)

