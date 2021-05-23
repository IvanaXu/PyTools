# -*-coding:utf-8-*-
# @auth ivan
# @time 2021-05-23 18:08:23
# @goal Test the Sqlite3 demo1

import sqlite3
with sqlite3.connect("109.Test_Sqlite3.db") as conn:
    c = conn.cursor()
    SQL = "SELECT sqlite_version() AS 'SQLite Version'"
    cursor = c.execute(SQL)
    for row in cursor:
        print(row)
    conn.commit()

with sqlite3.connect(":memory:") as conn:
    c = conn.cursor()
    SQL = "SELECT sqlite_version() AS 'SQLite Version'"
    cursor = c.execute(SQL)
    for row in cursor:
        print(row)
    conn.commit()
