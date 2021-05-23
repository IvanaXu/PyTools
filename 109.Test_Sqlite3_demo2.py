# -*-coding:utf-8-*-
# @auth ivan
# @time 2021-05-23 18:18:23
# @goal Test the Sqlite3 demo2

import random
import sqlite3
import pandas as pd

# 数据连接
conn = sqlite3.connect(":memory:")

# 数据导出 
data = pd.DataFrame(
    [
        [
            random.randint(0,9), 
            random.randint(0,9), 
            random.randint(0,9),
        ] 
        for _ in range(5)
    ], 
    columns=["A", "B", "C"]
)
data.to_sql("data", conn)
print(data)

# 数据读取
SQL = """
SELECT 
    *,
    (SELECT SUM(A) FROM data) AS SUMA
FROM data
JOIN (
    SELECT MIN(B) AS MINB
    FROM data
)
"""
print(pd.read_sql(SQL, conn))
