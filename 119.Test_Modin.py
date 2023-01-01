import time
import random
import pandas as pd
from tqdm import tqdm
import modin.pandas as pm


csv = "/track/119.Test_Modin.csv"

def calT(ptask):
    calTr = []

    time0 = time.time()
    df = ptask.read_csv(csv)
    calTr.append(time.time()-time0)
    # print(0)

    time1 = time.time()
    df.isnull()
    calTr.append(time.time()-time1)
    # print(1)

    time2 = time.time()
    df.apply(lambda x: x/x.mean())
    calTr.append(time.time()-time2)
    # print(2)

    return calTr


result = []
for rows, cols in tqdm([
    [10000, 10000],
    [1000, 1000],
    [100, 100],
    [10, 10]
]):
    df = pd.DataFrame([
        [
            random.random() 
            for i in range(cols)
        ]
        for j in range(rows)
    ])

    df.to_csv(csv, index=None)

    result.append([rows, cols] + calT(pd) + calT(pm))


result = pd.DataFrame(
    result, columns=["Rows", "Cols", "pdT1", "pdT2", "pdT3", "pmT1", "pmT2", "pmT3"])
for n in [1, 2, 3]:
    result[f"upT{n}"] = result[f"pmT{n}"]/result[f"pdT{n}"]
result
