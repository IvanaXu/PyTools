# -*- coding:utf-8 -*-
# @auth ivan
# @time 2020-06-08
# @goal Test the difflib

import difflib
s1 = "Test the difflib"
s2 = "Test the python"

for _ in difflib.SequenceMatcher(None, s1, s2).get_matching_blocks():
    if _.size > 3:
        print(s1[_.a: _.a+_.size])
# Test the XXX



