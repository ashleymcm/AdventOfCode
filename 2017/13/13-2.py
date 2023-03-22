def trip_severity(delay):
    severity = 0
    last_wall = -1
    wall_array = []
    directions = []

    # comment comment comment
    with open("input.txt") as wall_list:
        walls = [walls.split() for walls in wall_list]

    # comment comment comment
    for wall in walls:
        # more comment
        wall_depth = int(wall[0].replace(":", ""))
        wall_range = int(wall[1])

        while last_wall != wall_depth - 1:
            wall_array.append("")
            directions.append("+")
            last_wall += 1
        dummy_string = list('x' * wall_range)
        dummy_string[0] = 's'
        wall_array.append(dummy_string)
        directions.append("+")
        last_wall += 1

    for i in range(delay):
        for i in range(len(wall_array)):
            wall = wall_array[i]
            direction = directions[i]
            if len(wall) > 0:
                ind = wall.index("s")

                if (direction == "+"):
                    if ind < len(wall) - 1:
                        wall[ind + 1] = 's'
                    else:
                        directions[i] = '-'
                        wall[ind - 1] = 's'
                else:
                    if ind > 0:
                        wall[ind - 1] = 's'
                    else:
                        directions[i] = '+'
                        wall[ind + 1] = 's'
                wall[ind] = 'x'

    for i in range(len(wall_array)):

        if len(wall_array[i]) > 0 and wall_array[i][0] == "s":
            severity = 1
            break

        for i in range(len(wall_array)):
            wall = wall_array[i]
            direction = directions[i]
            if len(wall) > 0:
                ind = wall.index("s")

                if (direction == "+"):
                    if ind < len(wall) - 1:
                        wall[ind + 1] = 's'
                    else:
                        directions[i] = '-'
                        wall[ind - 1] = 's'
                else:
                    if ind > 0:
                        wall[ind - 1] = 's'
                    else:
                        directions[i] = '+'
                        wall[ind + 1] = 's'
                wall[ind] = 'x'

    return severity


delay = 9
severity = -1
while severity != 0:
    delay += 1
    severity = trip_severity(delay)


print(delay)
