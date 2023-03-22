import os, sys

# i hate that i need this when i'm on my windows machine
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

# loop through input rows, or "depths"
with open(os.path.join(dirname, "input.txt")) as depths_list:
  depths = [int(depths) for depths in depths_list]

def countDepthIncreases(depths):
  # initialize counter
  increases = 0
  
  # set first depth to first item in list and pop it off
  previousDepth = depths.pop(0)

  for depth in depths:
    if depth > previousDepth:
      increases += 1
    previousDepth = depth

  return increases

# print result
print(countDepthIncreases(depths))