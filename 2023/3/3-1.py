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

# a helper function that helps determine if a part is "valid" or not. we're essentially taking
# all the chars surrounding a number and adding them to a single string which is then searched
# to see if it contains a character that isn't ".". If so then it is "valid"
def is_valid_part_in_engine(engine_rows, part):
    string_to_search = ""
    # we look one char to the left if possible, otherwise 0
    if part.x_start > 0:
        x_start = part.x_start - 1
        string_to_search += engine_rows[part.y][x_start]
    else:
        x_start = 0
    
    # we look one char to the right if possible, otherwise last char in row
    if part.x_end < len(engine_rows[0]) - 1:
        x_end = part.x_end + 1
        string_to_search += engine_rows[part.y][x_end]
    else:
        x_end = len(engine_rows[0]) - 1

    # we start at the row above (if it exists), starting one char earlier and ending
    # one char later than the part because "diagonals" count
    if part.y > 0:                                                      # we add one here because
        string_to_search += engine_rows[part.y - 1][x_start:x_end + 1]  # this end is exclusive,
                                                                        # so it actually ends one before
    # lastly and similarly, we look at the row below (if it exists)
    if part.y < len(engine_rows) - 1:                                   # similar to above, we add one
        string_to_search += engine_rows[part.y + 1][x_start:x_end + 1]  # here because it is exclusive

    # now we search the string to see if there are any symbols in there. if yes
    # then this is a valid part
    for char in string_to_search:
        if char != ".":
            return True
        
    return False
    

# take the engine document and split it in an array of rows
with open("input.txt") as engine:
    engine_rows = engine.read().strip().split("\n")

# loop through engine_rows to find all existing parts
parts = []
for i in range(len(engine_rows)):
    parts += find_parts(engine_rows[i], i)

# determine which parts are actually valid
valid_parts = []
for part in parts:
    if (is_valid_part_in_engine(engine_rows, part)):
        valid_parts.append(part)

# loop through valid_parts to add their values to the sum
parts_sum = 0
for part in valid_parts:
    parts_sum += part.value

# now we have what we're looking for
print(parts_sum)


