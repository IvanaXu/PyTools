import os
import pandas as pd

data = []
TASK = sorted(
    [i for i in os.listdir() if "3." in i],
    key=lambda x: float(x.replace("3.", ""))
)
for t in TASK:

    t1, t2, tdata = "", "", {}
    with open(f"{t}/py{t}.log") as f:
        for i in f:
            i = i.strip("\n")
            
            if "###" in i:
                t1 = i.replace("###", "").replace(" ", "")
            if "Mean" in i:
                t2 = i.replace("Mean +- std dev: ", "")
                tdata[t1] = t2

                t1, t2 = "", ""

    tdata = pd.DataFrame(
        [[_k, _v] for _k, _v in tdata.items()],
        columns=["Task", t]
    )
    data.append(tdata)

sdata = pd.DataFrame()
for tdata in data:
    if len(sdata) == 0:
        sdata = tdata
    else:
        sdata = pd.merge(sdata, tdata, on="Task", how="outer")


def fchange(string):
    if pd.isna(string):
        return string
    string = str(string).split("+-")[0]

    result = -999999
    if "sec" in string:
        result = float(string.replace("sec", ""))*1000
    elif "ms" in string:
        result = float(string.replace("ms", ""))
    elif "us" in string:
        result = float(string.replace("us", ""))/1000
    elif "ns" in string:
        result = float(string.replace("ns", ""))/1000/1000
    return round(result, 4)

def change(df):
    _df = df.copy()
    for icol in TASK:
        _df[icol] = _df[icol].apply(fchange)
    return _df

cdata = change(sdata)
cdata0 = cdata.copy()
cdata.loc["SUM"] = [""] + [round(cdata0[icol].sum(), 4) for icol in  TASK]
cdata.loc["AVG"] = [""] + [round(cdata0[icol].mean(), 4) for icol in  TASK]

with open("compare.md", "w") as f:
    f.write("### 0.Source\n")
    for i in sdata.fillna("/").to_markdown():
        f.write(i)
    f.write("\n\n")

    f.write("### 1.Change\n")
    for i in cdata.fillna("/").to_markdown():
        f.write(i)
    f.write("\n\n")
    