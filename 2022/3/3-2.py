import os, sys, maps
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

def findRepeatedItem(rucksack_1, rucksack_2, rucksack_3):
  #should always be 1, so grab at index 0
  return list(set(rucksack_1) & set(rucksack_2) & set(rucksack_3))[0]

def findPrioritySum(rucksacks):
  total = 0
  for i in range(len(rucksacks))[2::3]:
    total += maps.priority_map[findRepeatedItem(rucksacks[i], rucksacks[i-1], rucksacks[i-2])]
  return total

with open(os.path.join(dirname, "input.txt")) as rucksack_list:
  rucksacks = rucksack_list.read().split("\n")
  print(findPrioritySum(rucksacks))