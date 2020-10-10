# 036.Test_Demo_N01.py
import re
import requests
cont = requests.get("https://m.maigoo.com/news/485519.html").content.decode(
    "utf-8")
pattern = re.compile(r'[\u4e00-\u9fa5]+')
for i in cont.split("\n"):
    s1 = """<td class="md_td">"""
    if s1 in i and pattern.search(i):
        print(i[i.find(s1) + len(s1):-5])
