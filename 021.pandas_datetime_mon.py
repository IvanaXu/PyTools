# -*-coding:utf-8-*-
# @auth ivan
# @time 2019-09-26 18:17
# @goal test pandas datetime

import pandas as pd
df = pd.DataFrame([
    ["20180101", "20180102"],
    ["20180101", "20180706"],
    ["20181001", "20190106"],
],
                  columns=["SDate0", "EDate0"])
print(df)

# 1 change and slice
df['SDate1'] = pd.to_datetime(df['SDate0'])
df['SDate2'] = df['SDate1'].dt.strftime('%Y%m%d')
df['SMon'] = df['SDate2'].str.slice(0, 6)
print(df)


# 2 date mon
def func(d1, d2):
    import datetime
    d1 = datetime.datetime.strptime(d1, "%Y%m%d")
    d2 = datetime.datetime.strptime(d2, "%Y%m%d")
    return (d2.year - d1.year) * 12 + (d2.month - d1.month)


df['GapMON_SEDate'] = [func(i, j) for i, j in zip(df["SDate0"], df["EDate0"])]
print(df)
