import math

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
    if [x, y] in infected_coordinates:
        index = infected_coordinates.index([x, y])
        #print("index", index)

        del infected_coordinates[index]
        direction = turn_right(direction)
    else:
        #print(x, y)
        infected_coordinates.append([x, y])
        direction = turn_left(direction)
        infected = True
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
with open("input.txt") as grid_file:
    grid = [list(row.strip()) for row in grid_file]

for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == '#':
            infected_coordinates.append([i, j])

x = math.floor(len(grid)/2)
y = x
direction = "up"
count = 0

for i in range(10000):
    infected = False
    infected_coordinates, direction, infected = toggle_node_and_turn(infected_coordinates, x, y, direction)
    if infected:
        count += 1
    x, y = move(x, y, direction)

print(count)
