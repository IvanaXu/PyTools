import os
path = r"C:\Users\IvanXu\Anaconda3\Scripts"

# 00.Make trun.spec
os.system(path + r"\pyi-makespec.exe -F run.py --name trun")

# 01.Change trun.spec to run.spec
rfile = open("run.spec", "w")
rfile.write("import sys\n")
rfile.write("sys.setrecursionlimit(9999)\n")
with open("trun.spec", "r") as f:
    for i in f:
        rfile.write(i)
rfile.close()

# 02.pyinstaller run.spec to exe
os.system(path + r"\pyinstaller.exe -F run.spec")

# 03.Test Run
os.system(r"dist\trun.exe")