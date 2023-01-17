import nude
from nude import Nude

for i in [1, 2, 3, 4]:
    n = Nude(f"134.Test_nudepy_{i}.jpg")
    n.parse()
    print(i, "damita :", n.result, n.inspect())
