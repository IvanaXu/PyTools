#
import time
import random
from tqdm import tqdm
from lxml import etree


n_web = lambda x: ["" if xi == 1 else f"{xi}/" for xi in range(1, x+1)]

d_web = {
    "服装品牌": n_web(977),
    "鞋业品牌": n_web(101),
    "皮具箱包": n_web(76),
    "美食餐饮": n_web(204),
    "母婴": n_web(165),
    "配饰": n_web(123),
    "化妆美容": n_web(34),
    "家纺家饰": n_web(47),
    "家居": n_web(79),
    "休闲娱乐": n_web(4),
    "教育加盟": n_web(5),
    "生活服务": n_web(3),
    "文创品牌": n_web(3),
}

# https://udger.com/resources/ua-list#Browser
d_hea = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 115Browser/8.6.2",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; 2345Explorer 5.0.0.14136)",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17 QIHU 360EE",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.8.0.5) Gecko/20060819 Firefox/1.5.0.5",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT)",
    "Opera/9.80 (Windows NT 5.1) Presto/2.12.388 Version/12.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-HK) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
]
l_hea = len(d_hea)-1

seq = "@_@"
s3 = """<pclass="first"><span>"""
s4 = """</span>"""
s5 = """target="_blank">"""
s6 = """<ahref="""
s7 = """<pclass="last"><i>"""
n_bad = 0


for i, j in tqdm(d_web.items(), desc="All"):
    f = open(f"Web/result_{i}.csv", "w")

    for ij in tqdm(j, desc=f"C{i}"):

        try:
            import requests
            cont = requests.get(
                f"http://www.chinasspp.com/brand/{i}/{ij}",
                headers={'User-Agent': d_hea[random.randint(0, l_hea)]}
            ).content.decode("gbk")

            tree = etree.HTML(cont)
            i_tree = tree.xpath("""//*[@id="container"]/*[@class="l"]/*[@class="brand"]""")
            for t1 in i_tree:
                t2 = etree.tostring(t1, encoding='utf-8').decode()
                t2 = t2.replace("\n", "").replace(" ", "").replace("&#13;", "")
                t2 = t2[t2.find(s3):]

                t2_1 = t2[t2.find(s3) + len(s3):t2.find(s4)] + seq
                t2 = t2[t2.find(s5) + len(s5):]

                t2_2 = t2[:t2.find(s6)].replace("</a>", seq).replace("</p><p>", seq) + seq

                t2_3 = t2[t2.find(s7) + len(s7):].replace("</i>", seq).replace("</p></div>", "\n")

                f.write(f"{t2_1}{t2_2}{t2_3}".replace(" ", ""))

            del requests
            time.sleep(random.random())
        except Exception as e:
            n_bad += 1
            print(f">>> {n_bad}, {e.args}")
    f.close()

# All: 100%|██████████| 13/13 [49:20<00:00, 70.87s/it]
# C服装品牌: 100%|██████████| 977/977 [22:49<00:00,  1.15s/it]
# C鞋业品牌: 100%|██████████| 101/101 [02:35<00:00,  1.09it/s]
# C皮具箱包: 100%|██████████| 76/76 [02:04<00:00,  2.44s/it]
# C美食餐饮: 100%|██████████| 204/204 [06:51<00:00,  1.55s/it]
# C母婴: 100%|██████████| 165/165 [06:34<00:00,  4.32s/it]
# C配饰: 100%|██████████| 123/123 [02:39<00:00,  1.84s/it]
# C化妆美容: 100%|██████████| 34/34 [00:36<00:00,  3.68s/it]
# C家纺家饰: 100%|██████████| 47/47 [01:29<00:00,  1.56s/it]
# C家居: 100%|██████████| 79/79 [02:15<00:00,  1.50s/it]
# C休闲娱乐: 100%|██████████| 4/4 [00:02<00:00,  1.78it/s]
# C教育加盟: 100%|██████████| 5/5 [00:03<00:00,  1.29it/s]
# C生活服务: 100%|██████████| 3/3 [01:03<00:00, 13.57s/it]
# C文创品牌: 100%|██████████| 3/3 [00:15<00:00, 10.34s/it]
# >>> 6, ()



