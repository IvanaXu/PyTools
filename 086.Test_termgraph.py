# -*-codinng:utf-8-*-
# @auth ivan
# @time 20201125
# @goal test termgraph
import os

#
os.system("""
termgraph 086.Test_termgraph_ex1.dat
""")

#
os.system("""
termgraph 086.Test_termgraph_ex1.dat --custom-tick "🏃" --width 20 --title "Running Data"
""")

#
os.system("""
echo "Label,3,9,1" | termgraph --custom-tick "😀" --no-label
""")

#
os.system("""
termgraph 086.Test_termgraph_ex4.dat  --color {blue,red}
""")

#
os.system("""
termgraph 086.Test_termgraph_ex7.dat --color {yellow,magenta} --stacked --title "Stacked Data"
""")

#
os.system("""
termgraph --calendar --start-dt 2017-07-01 086.Test_termgraph_cal.dat
""")
