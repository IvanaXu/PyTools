import re
import requests
cont = requests.get("https://m.maigoo.com/news/486050.html").content.decode("utf-8")
pattern = re.compile(r'[\u4e00-\u9fa5]+')
for i in cont.split("\n"):
    s1 = """html" title="""
    if s1 in i and pattern.search(i):
        print(i[i.find(s1)+len(s1)+1:-2])

    s21 = """html" >"""
    s22 = """</a></td>"""
    if s21 in i and s22 in i and pattern.search(i):
        print(i[i.find(s21)+len(s21):-len(s22)])
