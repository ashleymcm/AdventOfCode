import math, bisect

def bisect_search(list, coordinate):
    """
    search using bisect()
    no-match gives closest index (no index error)
    """
    ix = bisect.bisect(list, coordinate) - 1
    sf = "Bisect search for {}, found it at index {}"
    # this will trap the no-match situation
    if ix > -1 and list[ix] == coordinate:
        return ix
    else:
        return -1

def turn_right(direction):
    if direction == "up":
        return "right"
    elif direction == "right":
        return "down"
    elif direction == "down":
        return "left"
    elif direction == "left":
        return "up"

def turn_left(direction):
    return turn_right(turn_right(turn_right(direction)))

def toggle_node_and_turn(infected_coordinates, x, y, direction):
    infected = False
    index = bisect_search(infected_coordinates, [x, y])
    if index > -1:
        del infected_coordinates[index]
        bisect.insort(flagged_coordinates, [x, y])
        direction = turn_right(direction)
        return infected_coordinates, direction, infected

    index = bisect_search(flagged_coordinates, [x, y])
    if index > -1:
        del flagged_coordinates[index]
        direction = turn_left(turn_left(direction))
        return infected_coordinates, direction, infected

    index = bisect_search(weakened_coordinates, [x, y])
    if index > -1:
        del weakened_coordinates[index]
        bisect.insort(infected_coordinates, [x, y])
        infected = True
        return infected_coordinates, direction, infected

    bisect.insort(weakened_coordinates, [x, y])
    direction = turn_left(direction)
    return infected_coordinates, direction, infected



def move(x, y, direction):
    if direction == "up":
        return x - 1, y
    elif direction == "right":
        return x, y + 1
    elif direction == "down":
        return x + 1, y
    elif direction == "left":
        return x, y - 1

infected_coordinates = []
flagged_coordinates = []
weakened_coordinates = []

with open("input.txt") as grid_file:
    grid = [list(row.strip()) for row in grid_file]

for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == '#':
            infected_coordinates.append([i, j])

infected_coordinates.sort()

x = math.floor(len(grid)/2)
y = x
previous_direction = "up"
direction = "up"
count = 0

for i in range(10000000):
    infected = False
    infected_coordinates, direction, infected = toggle_node_and_turn(infected_coordinates, x, y, direction)
    if infected:
        count += 1
    x, y = move(x, y, direction)

print(count)
