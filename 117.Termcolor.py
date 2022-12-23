#
import random
from termcolor import cprint
"""
Available text colors:
  red, green, yellow, blue, magenta, cyan, white.

Available text highlights:
  on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.
"""


for i in range(10):
   num = random.randint(111111, 999999)
   
   if num%10 == 0:
      cprint(num, "red", "on_green")
   elif num%10 == 1:
      cprint(num, "green", "on_red")
   elif num%10 == 2:
      cprint(num, "yellow", "on_blue")
   elif num%10 == 3:
      cprint(num, "blue", "on_yellow")
