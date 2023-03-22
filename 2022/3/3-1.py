import os, sys, maps
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

def findRepeatedItem(rucksack):
  rucksack_size = len(rucksack)
  compartment_size = rucksack_size//2
  first_compartment, second_compartment = rucksack[:compartment_size], rucksack[compartment_size:]
  return list(set(first_compartment) & set(second_compartment))[0] #should always be 1, so grab at index 0

def findPrioritySum(rucksacks):
  total = 0
  for rucksack in rucksacks:
    total += maps.priority_map[findRepeatedItem(rucksack)]
  return total

with open(os.path.join(dirname, "input.txt")) as rucksack_list:
  rucksacks = rucksack_list.read().split("\n")
  print(findPrioritySum(rucksacks))