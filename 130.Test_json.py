import time
from tqdm import tqdm


# 
import json
with open("130.Test_json_base.json", "r") as f:
    _r = json.load(f)
    print(_r)

_result = {}
for i in tqdm(list("ABCDEFGHIJKLMN")):
    _result[i] = _r

with open("130.Test_json.json", "w") as f:
    json.dump(_result, f)
    
    
#
import json as j
time0 = time.time()
with open("130.Test_json.json", "r") as f:
    _r = j.load(f)
    print(_r.keys())
time1 = time.time()
print(f"json {time1-time0:.6f}s")


import simplejson as j
time0 = time.time()
with open("130.Test_json.json", "r") as f:
    _r = j.load(f)
    print(_r.keys())
time1 = time.time()
print(f"simplejson {time1-time0:.6f}s")


import ujson as j
time0 = time.time()
with open("130.Test_json.json", "r") as f:
    _r = j.load(f)
    print(_r.keys())
time1 = time.time()
print(f"ujson {time1-time0:.6f}s")

