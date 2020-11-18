#!/usr/bin/env python
# coding: utf-8
import ibm_db
import ibm_db_dbi
import pandas as pd
from sqlalchemy import create_engine

# method1
connStr = "DATABASE=sample;HOSTNAME=0.0.0.0;PORT=50000;PROTOCAL=TCPIP;UID=db2inst1;PWD=db2inst1-pwd;"
con = ibm_db.connect(connStr, "", "")
#
SQL = """
DROP TABLE ACT_T;
CREATE TABLE ACT_T LIKE ACT;
INSERT INTO ACT_T SELECT * FROM ACT;
COMMIT;
"""

SQL = SQL.replace("\t", "").replace("\n", "")
SQL = [_ for _ in SQL.split(";") if _]
for iSQL in SQL:
    try:
        run = ibm_db.exec_immediate(con, iSQL)
    except Exception as e:
        print(e)

# method2
engine = create_engine(
    'db2+ibm_db://db2inst1:db2inst1-pwd@0.0.0.0:50000/sample')
dt = "../Data/TestRisk"
data = pd.read_csv(f"{dt}/train.csv")

for _ in range(1):
    g, st, ed = 100, 0, 0
    for i in tqdm(range(100)):
        st, ed = st, st + g
        data.iloc[st:ed].to_sql(
            'tdata', engine, index=False, if_exists="append")
        st = ed
