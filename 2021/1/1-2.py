import os, sys

# i hate that i need this when i'm on my windows machine
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

# loop through input rows, or "depths"
with open(os.path.join(dirname, "input.txt")) as depths_list:
  depths = [int(depths) for depths in depths_list]

def calculateGroupSum(index, depths):
  return depths[index] + depths[index + 1] + depths[index + 2]

def countDepthIncreases(depths):
  # initialize counter
  increases = 0

  # initialize first sum
  previousSum = calculateGroupSum(0, depths)
  
  for i in range(1, len(depths) - 2):
    currentSum = calculateGroupSum(i, depths)
    if currentSum > previousSum:
      increases += 1
    previousSum = currentSum

  return increases

# print result
print(countDepthIncreases(depths))