# -*-coding:utf-8-*-
# @auth ivan
# @time 20181230
# @goal tPatterns the json
import json
info = """callback({"status":"1","info":"OK","infocode":"10000","count":"1","geocodes":[{"formatted_address":"
广东省广州市黄埔区茅岗路|1103","country":"中国","province":"广东省","citycode":"020","city":"广州市",
"district":"黄埔区","township":[],"neighborhood":{"name":[],"type":[]},"building":{"name":[],"type":[]},
"adcode":"440112","street":"茅岗路","number":"1103","location":"113.439877,23.124785",
"level":"门牌号"}]})""".replace('\n', '')
call_str = 'callback('
json_str = 'geocodes'
info_json = json.loads(info[info.find(call_str)+len(call_str):-1])[json_str][0]
for j in info_json:
    info_json[j] = str(info_json[j])
print(info_json)

# import json
# with open("data.txt", "r", encoding="gbk") as f:
#     data = f.readlines()
# json_file = data[0]
# j_obj = json.loads(json_file)
# print(j_obj)
# print(j_obj["decisionResult"])
# print(j_obj["decisionResult"].keys())
# for i, j in j_obj["decisionResult"].items():
#     print(i, j)
