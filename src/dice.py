"""
This file contains commands relating to rolling a dice
"""

# Package imports
import random

def roll(arg):
  result_list = []
  for i in range(len(arg)):
    if arg[i][0] == 'd':
      die = int(arg[i].strip('d'))
      result = random.randint(1, die)
    elif arg[i] == '+':
      result += int(arg[i+1])
    elif arg[i] == '-':
      result -= int(arg[i+1])
    result_list.append(result)
  return result_list