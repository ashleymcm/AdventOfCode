import os, sys, math
from collections import Counter

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "<Coordinate x:%s y:%s>" % (self.x, self.y)

class Point:
    def __init__(self, x, y, closest):
        self.coordinate = Coordinate(x, y)
        self.closest = closest
    def __repr__(self):
        return "<Point x:%s y:%s closest:%s>" % (self.coordinate.x, self.coordinate.y, self.closest)

def manhatten_distance(x, y, a):
    return math.fabs(a.x - x) + math.fabs(a.y - y)

def closest(x, y, coordinates):
    smallest = manhatten_distance(x, y, coordinates[0])
    closest = 0
    for i in range(1, len(coordinates)):
        coordinate = coordinates[i]
        distance = manhatten_distance(x, y, coordinate)
        #print(x, y, coordinate.x, coordinate.y, distance)
        if distance < smallest:
            smallest = distance
            closest = i
        elif smallest == distance:
            closest = -1
    return closest

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

##create grid of all points within these max and min and find their
##closest coordinate
points = []
for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        ##if it's on the edge it'll be part of an infinite group, 
        ##so just set to -1 from the get go
        if x == min_x or x == max_x or y == min_y or y == max_y:
            points.append(Point(x, y, -1))
        else:
            points.append(Point(x, y, closest(x, y, coordinates)))

##create list of points' closest coordinate (ignoring -1)
#####NOTE: by ignoring -1 this is kind of hacky because we're assuming (hoping?) that
########## by excluding edge area the largest non-infinite area will be, by default, 
########## larger. This may not always give the right solution but in this case it did.
distances = []
for point in points:
    if point.closest > -1:
        distances.append(point.closest)

##find the most common closest coordinate and print the count of its number of occurrences
data = Counter(distances)
idx = max(distances, key=data.get)
print(data[idx])