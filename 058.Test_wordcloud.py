# -*-coding:utf-8-*-
# @auth ivan
# @time 2020-07-16
# @goal test wordcloud
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

words = """
支付宝
财付通
转入
网银
人行
银联
超市
酒店
商贸
销售
科技
贸易
京东
百货
汽车
服饰
美容
餐厅
食品
国际
便利店
化妆品
建材
特约
加油站
文化
个体户
烟酒
家具
电器
生活
装饰
珠宝
健身
分期
广场
酒吧
药房
旅行
养生
家电
娱乐
火锅
教育
百货
电子
五金
批发
餐馆
网络
咨询
水果
专卖店
海鲜
万达
生鲜
石油
酒楼
母婴
美食
通讯
阳光
食品
足浴
KTV
传播
按摩
材料
摄影
工程
数码
医药
烧烤
面馆
洗浴
小吃
商务酒店
美容美发
购物
蔬菜
保健
麻辣烫
眼镜
咖啡
牛肉
维修
商场
皮具
快餐
手机
电脑
烤肉
箱包
女装
童装
医疗
儿童
艺术
饮品
音乐
设计
主题
美体
数据
决策
analytics
数据挖掘
Machine Learning
Data
Artificial
SAS
Python
信用卡
乐驾卡
标准白金
寰宇
Master
Visa
"""
words = words.split("/n")

new_worlds = " ".join(words)
coloring = np.array(Image.open("058.Test_wordcloud_in.jpg"))

# simkai.ttf !!! Chinese
my_wordcloud = WordCloud(
    background_color="white", max_words=800,
    mask=coloring, max_font_size=120, random_state=40, scale=2,
    font_path="058.Test_wordcloud_simkai.ttf"
).generate(new_worlds)

my_wordcloud.to_file('058.Test_wordcloud_ot.jpg')


