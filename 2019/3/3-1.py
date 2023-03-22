import os, sys, math

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

##loop through wire directions
with open(os.path.join(dirname, "input.txt")) as wire_dirs_list:
    wires = [dirs.split(",") for dirs in wire_dirs_list]

def calcManhattanDistance(coord):
    return abs(coord[0]) + abs(coord[1])

def minManhattanDistance(coords):
    min = None
    for coord in coords:
        dist = calcManhattanDistance(coord)
        if (min is None or dist < min):
            min = dist

    return min

def calcCoordinates(wire):
    coords = [(0,0)]
    for dir in wire:
        coords = coords + addDirCoords(coords.pop(), dir.strip())
    return coords

def addDirCoords(coord, dir):
    coords = []
    direction = dir[0]
    length = int(dir[1:])
    x = coord[0]
    y = coord[1]

    if direction == 'U':
        for z in range(length + 1):
            coords.append((x, y + z))
    elif direction == 'D':
        for z in range(length + 1):
            coords.append((x, y - z))
    elif direction == 'R':
        for z in range(length + 1):
            coords.append((x + z, y))
    elif direction == 'L':
        for z in range(length + 1):
            coords.append((x - z, y))
    return coords

wire1coords = set(calcCoordinates(wires[0]))
wire2coords = set(calcCoordinates(wires[1]))
intersections = wire1coords.intersection(wire2coords)
intersections.remove((0,0))

print(minManhattanDistance(list(intersections)))

