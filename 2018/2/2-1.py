import os, sys
from collections import Counter

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

##loop through input rows, or "box IDs"
with open(os.path.join(dirname, "input.txt")) as box_id_list:
    box_ids = [box_ids.split() for box_ids in box_id_list]

count_2 = 0
count_3 = 0

for box_id in box_ids:
    counter = Counter(box_id[0])
    is_2 = False
    is_3 = False

    ##loop through count of each letter in the ID and set variables to True if count is correct
    for letter, count in counter.items():
        if count == 2:
            is_2 = True
        elif count == 3:
            is_3 = True

    ##add to counts if variables were set to True
    if is_2:
        count_2 += 1
    if is_3:
        count_3 += 1

##print product of both counts as the "checksum"
print(count_2 * count_3)