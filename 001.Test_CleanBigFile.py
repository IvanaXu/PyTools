# -*- coding:utf-8 -*-
# @auth ivan
# @time 2018-07-16 11:45:41
# @goal clean the big file
#

import os
import pandas as pd
root_list = ['/data/project/Temp']
result = []

# IF NOT os.walk, YOU CAN USE THE os.listdir
print("Start!")
for root in root_list:
    for i, j, k in os.walk(root):
        for t in k:
            p = i + os.path.sep + t
            print(p)
            data = pd.DataFrame([[p, os.path.getsize(p)]],
                                columns=['File', 'Size'])
            result.append(data)
print("Finis!")
data_all = pd.DataFrame(pd.concat(result))
data_all.sort_values('Size', inplace=True)
print(data_all)
