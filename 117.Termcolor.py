import random
from termcolor import cprint
"""
Available text colors:
  red, green, yellow, blue, magenta, cyan, white.

Available text highlights:
  on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.
"""

for i in range(10):
   number = random.randint(111111, 999999)
   
   if number%10 == 0:
      cprint(number, "red", "on_green")
   elif number%10 == 1:
      cprint(number, "green", "on_red")
   elif number%10 == 2:
      cprint(number, "yellow", "on_blue")
   elif number%10 == 3:
      cprint(number, "blue", "on_yellow")
