# -*-coding:utf-8-*-
# @auth ivan
# @time 20200611
# @goal test Latitude and longitude distance

from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000


print(haversine(113.251028, 23.16372833, 113.250982, 23.163659))
# 9.030258216504823

# http://tool.yovisun.com/longlat
# 两点距离：9.0304026906347米
# 点1：纬度:23.16372833,经度:113.251028，点2：纬度:23.163659,经度:113.250982



