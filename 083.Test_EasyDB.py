# -*-coding:utf-8-*-
# @auth ivan
# @time 20201124
# @goal test easydb

import easydbio

db = easydbio.DB({
    "database": "d6e09f6a-8e4e-4de9-938c-baf79f953399",
    "token": "0cb4c6d7-def4-4187-a56a-27f82e2e2e9f"
})

db.Put("key", "8")
print(db.Get("key"))
print(db.List())
