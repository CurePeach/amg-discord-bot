"""
This file contains commands relating to rolling a dice.
"""

# Package imports
import random

def roll(arg):
  """
  TODO(gordon): function comment
  Note. something this function comment needs which the functions in 
  main.py don't need is describing what each parameter does. 
  """
  result_list = []
  total = i = 0
  while i < len(arg):
    # TODO(gordon): consider maybe having a parse function?
    if arg[i][0] == 'd':
      result, result_list = dice_roll(arg, i - 1, result_list)
      total += result
    elif arg[i] == '+':
      if arg[i+1][0] == 'd':
        result, result_list = dice_roll(arg, i, result_list)
        total += result
      elif len(arg[i+1]) > 1:
        mult_rolls = []
        for j in range(int(arg[i + 1][0])):
          result, mult_rolls = dice_roll(arg, i, mult_rolls)
          total += result
        result_list.append(mult_rolls)
      else:
        result = int(arg[i+1])  
        total += result
      i += 1
    elif arg[i] == '-':
      if arg[i+1][0] == 'd':
        result, result_list = dice_roll(arg, i, result_list)
        total -= result
      elif len(arg[i+1]) > 1:
        mult_rolls = []
        for j in range(int(arg[i + 1][0])):
          result, mult_rolls = dice_roll(arg, i, mult_rolls)
          total -= result
        result_list.append(mult_rolls)
      else:
        result = int(arg[i+1]) 
        total -= result
      i += 1
    elif len(arg[i]) > 1:
      if arg[i][1] == 'd':
        mult_rolls = []
        for j in range(int(arg[i][0])):
          result, mult_rolls = dice_roll(arg, i - 1, mult_rolls)
          total += result
        result_list.append(mult_rolls)
    if result == 0:
      return 0 , total
    i += 1
  return format_roll_string(result_list), total

def dice_roll(arg, index, array):
  """
  TODO(gordon): function comment
  """
  if arg[index + 1] != 'd':
    die = int(arg[index + 1][1:].strip('d'))
  else:
    die = int(arg[index + 1].strip('d'))
  if die < 2:
    result = 0
  else:
    result = random.randint(1, die)
    array.append(result)
  return result, array
  
def format_roll_string(result_list):
  """
  TODO(gordon): function comment
  """
  string_list = []
  for item in result_list:
    if isinstance(item, int):
      string_list.append(f"[{item}]")
    else:
      string_list.append(str(item))
  return ' '.join(string_list)