import os, sys
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

def getSumCaloriesPerElf(calories):
  calories = [int(calories) for calories in calories.split("\n")]
  return sum(calories)

def getSumOfTopThree(calories_per_elf):
  calories_per_elf.sort(reverse=True)
  top_three_elves = calories_per_elf[0:3]
  return sum(top_three_elves)

with open(os.path.join(dirname, "input.txt")) as calories_list:
  calories_per_elf = [getSumCaloriesPerElf(calories) for calories in calories_list.read().split("\n\n")]
  print(getSumOfTopThree(calories_per_elf))