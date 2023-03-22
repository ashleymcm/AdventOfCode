import os, sys, itertools, re

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def manhatten_distance(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def equals(self, point):
        return self.x == point.x and self.y == point.y and self.z == point.z

    def spit(self):
        print(self.x, self.y, self.z)


class Particle:

    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.collided = False

    def update(self):
        self.velocity.x += self.acceleration.x
        self.velocity.y += self.acceleration.y
        self.velocity.z += self.acceleration.z
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.position.z += self.velocity.z

    def equals(self, particle):
        return self.position.equals(particle.position) and self.velocity.equals(particle.velocity) and self.acceleration.equals(particle.acceleration)

    def colliding(self, particle):
        return self.position.equals(particle.position)

    def spit(self):
        self.position.spit()
        self.velocity.spit()
        self.acceleration.spit()


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

for j in range(100):
    collided = []

    for particle in particles:
        particle.update()

    for a, b in itertools.combinations(particles, 2):
        if a.colliding(b):
            a.collided = True
            b.collided = True

    for i in range(len(particles)):
        particle = particles[i]
        if particle.collided:
            collided.append(i)

    collided = list(set(collided))
    collided.sort(reverse = True)

    for i in collided:
        del particles[i]

print(len(particles))
