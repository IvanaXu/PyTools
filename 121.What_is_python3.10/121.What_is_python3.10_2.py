import pathlib
p = pathlib.Path()
p1 = p/"121.What_is_python3.10_2A.txt"
p2 = p/"121.What_is_python3.10_2B.txt"

with(
    p1.open(encoding="utf-8") as f1,
    p2.open(encoding="utf-8") as f2
):
    print(f1.read(), f2.read(), sep="\n") 
