import os, sys

# i hate that i need this when i'm on my windows machine
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

# loop through input rows, or "lines"
with open(os.path.join(dirname, "input.txt")) as lines_list:
  lines = [lines.rstrip().split(' -> ') for lines in lines_list]

def getLineEnds(line):
  pointA = [int(point) for point in line[0].split(',')]
  pointB = [int(point) for point in line[1].split(',')]

  return pointA, pointB

def getPointsInHorizontalLine(pointA, pointB):
  points = []

  y = pointA[1]
  
  if pointA[0] > pointB[0]:
    minX = pointB[0]
    maxX = pointA[0]
  else:
    minX = pointA[0]
    maxX = pointB[0]

  for x in range(minX, maxX + 1):
    points.append(str(x) + ',' + str(y))

  return points

def getPointsInVerticalLine(pointA, pointB):
  points = []

  x = pointA[0]

  if pointA[1] > pointB[1]:
    minY = pointB[1]
    maxY = pointA[1]
  else:
    minY = pointA[1]
    maxY = pointB[1]

  for y in range(minY, maxY + 1):
    points.append(str(x) + ',' + str(y))

  return points

def isVerticalLine(pointA, pointB):
  return pointA[0] == pointB[0]

def isHorizontalLine(pointA, pointB):
  return pointA[1] == pointB[1]
  
def addPointsToDict(points, dictionary):
  for point in points:
    if point in dictionary:
      dictionary[point] += 1
    else:
      dictionary[point] = 1

  return dictionary

def getPointsCount(lines):
  points = {}

  for line in lines:
    pointA, pointB = getLineEnds(line)
    
    if isHorizontalLine(pointA, pointB):
      addPointsToDict(getPointsInHorizontalLine(pointA, pointB), points)
    elif isVerticalLine(pointA, pointB):
      addPointsToDict(getPointsInVerticalLine(pointA, pointB), points)

  count = 0
  
  for key, value in points.items():
    if value > 1:
      count += 1

  return count

print(getPointsCount(lines))