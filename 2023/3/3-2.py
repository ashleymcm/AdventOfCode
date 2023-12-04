# a little class to hold the part information. not really needed for this right now
# but i like having the structure a little more formalized
class Part:
    def __init__(self, value, x_start, x_end, y):
        self.value = int(value)
        self.x_start = x_start
        self.x_end = x_end
        self.y = y

# a helper function that finds all the "parts" aka numbers in an engine row. it creats a
# Part object for each and adds them to a list which is returned at the end     
def find_parts(engine_row, row_idx):
    parts = []
    idx_start = -1
    for i in range(len(engine_row)):
        if not engine_row[i].isdigit() and idx_start < 0:
            continue
        elif not engine_row[i].isdigit() and idx_start >= 0:
            parts.append(Part(engine_row[idx_start:i], idx_start, i - 1, row_idx))
            idx_start = -1
        elif idx_start < 0:
            idx_start = i
    
    # if the row ended on a number we need to make sure we add it as well
    if engine_row[i].isdigit() and idx_start > 0:
        i = len(engine_row)
        parts.append(Part(engine_row[idx_start:i], idx_start, i - 1, row_idx))

    return parts

# a helper function that determines if the given coordinates of a * touch one
# or more parts, thus making it a gear, and if so returns its "ratio"
def if_gear_return_ratio(x, y, parts):
    touching_parts = [] # lol
    for part in parts:
        # we look one char to the left if possible, otherwise 0
        if part.x_start > 0:
            x_start = part.x_start - 1
        else:
            x_start = 0
        
        # we look one char to the right if possible, otherwise last char in row
        if part.x_end < len(engine_rows[0]) - 1:
            x_end = part.x_end + 1
        else:
            x_end = len(engine_rows[0]) - 1

        # we start at the row above (if it exists), starting one char earlier and ending
        # one char later than the part because "diagonals" count
        if part.y > 0:
            y_start = part.y - 1
        else:
            y_start = 0
        
        if part.y < len(engine_rows) - 1:
            y_end = part.y + 1
        else:
            y_end = part.y

        # now we search the area between x_start -> x_end and y_start -> y_end to see if
        # it overlaps with the coordinates of the gear. if yes, we add to the count
        if x_start <= x and x_end >= x and y_start <= y and y_end >= y:
            touching_parts.append(part)
     
     # if there are exactly two touching parts then these are gears and we can calculate
     # their "ratio" by multipling their values together       
    if (len(touching_parts) == 2):
        return touching_parts[0].value * touching_parts[1].value
    
    # otherwise just return 0 since this won't affect a future sum
    return 0
    

# take the engine document and split it in an array of rows
with open("input.txt") as engine:
    engine_rows = engine.read().strip().split("\n")

# loop through engine_rows to find all existing parts
parts = []
for i in range(len(engine_rows)):
    parts += find_parts(engine_rows[i], i)

# loop through chars to find gears and their ratios. this was a super non-performant
# way to do this part of the challenge but the way i did the first part didn't carry
# over well and i didn't really feel like redoing a bunch of this so i'm just going
# to kind of duct tape it together and then go to bed ¯\_(ツ)_/¯
ratio_sum = 0
for y in range(len(engine_rows)):
    for x in range(len(engine_rows[0])):
        char = engine_rows[y][x]
        if char == '*':
            ratio_sum += if_gear_return_ratio(x, y, parts)


# now we have what we're looking for
print(ratio_sum)


