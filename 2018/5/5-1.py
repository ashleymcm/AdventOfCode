import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

def is_same_type(a, b):
    return a.lower() == b.lower()

def is_opposite_polarity(a, b):
    return (a.islower() and b.isupper()) or (a.isupper() and b.islower())

def do_react(a, b):
    return is_same_type(a, b) and is_opposite_polarity(a, b)

polymer = ""
i = 0

##open file and store "polymer"
with open(os.path.join(dirname, "input.txt")) as fileobj:
    for line in fileobj:  
       for ch in line: 
           polymer += ch
           
##loop through polymer
while i < len(polymer):  
    ##if this is the last unit, then we can stop the loop
    if i >= len(polymer) - 1:
        break

    ##otherwise, continue checking for reactive units
    current_unit = polymer[i]
    next_unit = polymer[i + 1]

    ##if the units react, remove them and start over at previous unit (if exists)
    if do_react(current_unit, next_unit):
        polymer = polymer[:i] + polymer[i + 2:]
        if i > 0:
            i -= 1
        else:
            i = 0
    ##otherwise just go to next unit
    else:
        i += 1

print(len(polymer))

