# -*-coding:utf-8-*-
# @auth ivan
# @time 20201124 00:56:00
# @goal Test eval
cmd = """
import os
os.system('ls -l')
"""
code_object = compile(cmd, "", "exec")
print(code_object)
eval(code_object, {'__builtins__': {}})
