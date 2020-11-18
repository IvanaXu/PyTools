import sys
title = "074.Test_Pycuda"
name = sys.argv[1]
print(name)

with open(f"{title}_{name}.cu", "w") as f:
    f.write(f"\n")

with open(f"{title}_{name}.sh", "w") as f:
    f.write(f"nvcc {title}_{name}.cu -o {title}_{name}\n")
    f.write(f"./{title}_{name}\n")
