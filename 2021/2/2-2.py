import os, sys

# i hate that i need this when i'm on my windows machine
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

# loop through input rows, or "movements"
with open(os.path.join(dirname, "input.txt")) as movements_list:
  movements = [movements.split() for movements in movements_list]

def translateMovementToMath(movement, aim, x, y):
  direction = movement[0]
  magnitude = int(movement[1])

  # updated the math to include aim and other new instructions
  if direction == 'down':
    aim += magnitude
  elif direction == "up":
    aim -= magnitude
  elif direction == 'forward':
    x += magnitude
    y += aim * magnitude

  return aim, x, y

def getProduct(movements):
  # it said we start at 0 depth and 0 horizontal movement
  x = 0
  y = 0

  # now we have aim as well
  aim = 0

  for movement in movements:
    aim, x, y = translateMovementToMath(movement, aim, x, y)

  # return the product of end results because... it said so
  return abs(x * y)

print(getProduct(movements))