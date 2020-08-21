#
print("#1 continue")
for _ in [1, 2, 3]:
    if _ == 2:
        continue
    else:
        print(_)
    print(_, "_")
# #1 continue
# 1
# 1 _
# 3
# 3 _

# 
print("#2 pass")
for _ in [1, 2, 3]:
    if _ == 2:
        pass
    else:
        print(_)
    print(_, "_")
# #2 pass
# 1
# 1 _
# 2 _
# 3
# 3 _

#
print("#3 break")
for _ in [1, 2, 3]:
    if _ == 2:
        break
    else:
        print(_)
    print(_, "_")
# #3 break
# 1
# 1 _