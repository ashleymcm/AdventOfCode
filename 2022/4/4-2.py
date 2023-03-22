import os, sys
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

def formatAssignmentPair(pair):
  one_dimension_pair_list = pair.split(",")
  two_dimension_pair_list = [pair.split("-") for pair in one_dimension_pair_list]
  return two_dimension_pair_list

def sectionOverlapsOther(pair):
  pair[0] = [int(pair[0][0]), int(pair[0][1])]
  pair[1] = [int(pair[1][0]), int(pair[1][1])]
  if (
      (pair[0][0] == pair[1][0]) or 
      (pair[0][1] == pair[1][0]) or 
      (pair[0][0] == pair[1][1]) or 
      (pair[0][1] == pair[1][1])
  ):
    return True
  if (pair[0][0] < pair[1][0]) and (pair[1][0] < pair[0][1]):
    return True
  if (pair[0][0] > pair[1][0]) and (pair[0][0] < pair[1][1]):
    return True
  
  return False

def countNumberOfOverlappingSections(assignment_pairs):
  total = 0
  for pair in assignment_pairs:
    if sectionOverlapsOther(pair):
      total += 1
  return total

with open(os.path.join(dirname, "input.txt")) as assignment_pair_list:
  assignment_pairs = [formatAssignmentPair(pair) for pair in assignment_pair_list.read().split("\n")]
  print(countNumberOfOverlappingSections(assignment_pairs))