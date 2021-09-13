"""
This file contains commands relating to rolling a dice
"""

# Package imports
import random

def roll(arg):
  result_list = []
  total = i = 0
  while i < len(arg):
    if arg[i][0] == 'd':
      result, result_list = dice_roll(arg, i - 1, result_list)
      total += result
    elif arg[i] == '+':
      if arg[i+1][0] == 'd':
        result, result_list = dice_roll(arg, i, result_list)
      else:
        result = int(arg[i+1])  
      total += result
      i += 1
    elif arg[i] == '-':
      if arg[i+1][0] == 'd':
        result, result_list = dice_roll(arg, i, result_list)
      else:
        result = int(arg[i+1]) 
      total -= result
      i += 1
    elif len(arg[i]) > 1:
      if arg[i][1] == 'd':
        j = 0
        mult_rolls = []
        for j in range(int(arg[i][0])):
          result, mult_rolls = dice_roll(arg, i - 1, mult_rolls)
          total += result
        result_list.append(mult_rolls)
    i += 1
  return result_list, total

def dice_roll(arg, index, array):
  if arg[index + 1] != 'd':
    die = int(arg[index + 1][1:].strip('d'))
  else:
    die = int(arg[index + 1][1:].strip('d'))
  result = random.randint(1, die)
  array.append(result)
  return result, array
  