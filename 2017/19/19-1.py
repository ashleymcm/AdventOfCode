import os, sys, itertools

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
with open(os.path.join(dirname, "input.txt")) as grid:
    rows = [list(row) for row in grid]

end = False
row = 0
col = rows[0].index("|")
direction = "down"
letters = []
whitespace = {' ', '\n', '\r'}

while not end:
    #print(letters, direction, row, col, rows[row][col])
    if direction == "down":
        row += 1
    elif direction == "up":
        row -= 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1

    val = rows[row][col]

    if val == '+':
        if direction != "right" and col - 1 >= 0 and rows[row][col - 1]  not in whitespace:
            #print(rows[row][col - 1])
            direction = "left"
        elif direction != "left" and col + 1 < len(rows[row]) and rows[row][col + 1] not in whitespace:
            #print(rows[row][col + 1])
            direction = "right"
        elif direction != "down" and row - 1 >= 0 and rows[row - 1][col] not in whitespace:
            #print(rows[row - 1][col])
            direction = "up"
        elif direction != "up" and row + 1 < len(rows) and rows[row + 1][col] not in whitespace:
            #print(rows[row + 1][col])
            direction = "down"
    elif val == ' ' or val == '\n':
        end = True
    elif val != '|' and val != '-':
        letters.append(val)


print("".join(letters))
