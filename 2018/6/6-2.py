import os, sys, math
from collections import Counter

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "<Coordinate x:%s y:%s>" % (self.x, self.y)

class Point:
    def __init__(self, x, y, within_10000):
        self.coordinate = Coordinate(x, y)
        self.within_10000 = within_10000
    def __repr__(self):
        return "<Point x:%s y:%s within_10000:%s>" % (self.coordinate.x, self.coordinate.y, self.within_10000)

def manhatten_distance(x, y, a):
    return math.fabs(a.x - x) + math.fabs(a.y - y)

def within_10000(x, y, coordinates):
    total = 0
    for coordinate in coordinates:
        distance = manhatten_distance(x, y, coordinate)
        total += distance
    return total < 10000

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
coordinates = []

##collect all input, or "coordinates"
with open(os.path.join(dirname, "input.txt")) as coordinate_list:
    coordinate_strings = [coordinate_strings.split(", ") for coordinate_strings in coordinate_list]

##put the coordinates into a list of Coordinate objects
for coordinate_string in coordinate_strings:
    coordinates.append(Coordinate(int(coordinate_string[0]), int(coordinate_string[1])))

##find the max and min (x, y) values
min_x = coordinates[0].x
min_y = coordinates[0].y
max_x = coordinates[0].x
max_y = coordinates[0].y

for coordinate in coordinates:
    if coordinate.x < min_x:
        min_x = coordinate.x
    if coordinate.x > max_x:
        max_x = coordinate.x
    if coordinate.y < min_y:
        min_y = coordinate.y
    if coordinate.y > max_y:
        max_y = coordinate.y

##add one to the max values so they'll be included in the loop
max_x += 1
max_y += 1

##create grid of all points within these max and min and find if they are within
##the 10000 limit
points = []
for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        points.append(Point(x, y, within_10000(x, y, coordinates)))

##count how many are within the limit
within_10000 = 0
for point in points:
    if point.within_10000:
        within_10000 += 1

print(within_10000)