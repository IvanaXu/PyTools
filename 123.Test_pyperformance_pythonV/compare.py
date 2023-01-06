import pandas as pd

data = []
for t in ["3.9.0", "3.10.0", "3.11.0", "3.11.1"]:

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

with open("compare.md", "w") as f:
    for i in sdata.fillna("/").to_markdown():
        f.write(i)
