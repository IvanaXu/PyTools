# 
import pyarma as pa
A = pa.mat(4, 5)
B = pa.mat(4, 5)
C = A * B.t()
C.print("C:")

"""
TODO

C:
        0        0        0        0
        0        0        0        0
        0        0        0        0
        0        0        0        0
"""