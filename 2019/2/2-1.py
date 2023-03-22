import os, sys, math

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

##loop through input row, or "ints"
with open(os.path.join(dirname, "input.txt")) as ints_list:
    ints = [int(x) for x in [ints.split(",") for ints in ints_list][0]]

def prepInput():
    ints[1] = 12
    ints[2] = 2

def performAction(pos):
    if ints[pos] == 1:
        ints[ints[pos + 3]] = ints[ints[pos + 1]] + ints[ints[pos + 2]]
    elif ints[pos] == 2:
        ints[ints[pos + 3]] = ints[ints[pos + 1]] * ints[ints[pos + 2]]

def run():
    pos = 0
    while (ints[pos] != 99):
        performAction(pos)
        pos += 4

prepInput()
run()
print(ints[0])
