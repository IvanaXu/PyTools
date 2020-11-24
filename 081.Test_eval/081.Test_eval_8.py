# -*-coding:utf-8-*-
# @auth ivan
# @time 20201124 00:56:00
# @goal Test eval
print("Start")
cmd = """
[ c for c in ().__class__.__bases__[0].__subclasses__() if c.__name__ == "Quitter" ][0](0,'quit')()
"""
eval(cmd, {'__builtins__': {}})
print("End")
