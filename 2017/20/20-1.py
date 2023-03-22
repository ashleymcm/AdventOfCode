import os, sys, itertools, re

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def manhatten_distance(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

class Particle:

    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

def get_particle(string):
    result = re.search('p=<(.*)>, v', string)
    position_list = result.group(1).split(',')
    position = Point(int(position_list[0]), int(position_list[1]), int(position_list[2]))

    result = re.search('v=<(.*)>, a', string)
    velocity_list = result.group(1).split(',')
    velocity = Point(int(velocity_list[0]), int(velocity_list[1]), int(velocity_list[2]))

    result = re.search('a=<(.*)>', string)
    acceleration_list = result.group(1).split(',')
    acceleration = Point(int(acceleration_list[0]), int(acceleration_list[1]), int(acceleration_list[2]))

    return Particle(position, velocity, acceleration)

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
with open(os.path.join(dirname, "input.txt")) as grid:
    particles = [get_particle(row) for row in grid]

min_val = 0
min_index = 0

for i in range(len(particles)):
    if particles[i].acceleration.manhatten_distance() < min_val or min_val == 0:
        min_val = particles[i].acceleration.manhatten_distance()
        min_index = i

print(min_index)
