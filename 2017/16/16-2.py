def spin(programs, place):
    return programs[-place:] + programs[0:(len(programs) - place)]


def exchange(programs, placeA, placeB):
    valA = programs[placeA]
    valB = programs[placeB]
    programs[placeA] = valB
    programs[placeB] = valA
    return programs


def partner(programs, valA, valB):
    placeA = programs.index(valA)
    placeB = programs.index(valB)
    programs[placeA] = valB
    programs[placeB] = valA
    return programs


og_programs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", ]
programs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", ]
programs_list = []
count = 0
repeat = False

with open("input.txt") as steps_list:
    steps = steps_list.read().strip().split(',')

while "".join(programs) not in programs_list:
    programs_list.append("".join(programs))

    for step in steps:

        if step[0] == "s":
            programs = spin(programs, int(step[1:]))

        elif step[0] == "x":
            places = step[1:].split("/")
            programs = exchange(programs, int(places[0]), int(places[1]))

        elif step[0] == "p":
            places = step[1:].split("/")
            programs = partner(programs, places[0], places[1])
    count += 1
    # repeat = programs == og_programs
'''
print(count, len(programs_list))
print("".join(programs))
print(1000000000%count)
print((count-1) - 1000000000%(count-1))
print(programs_list[0], programs_list[count - 1])
print("".join(programs_list[1000000000%count]))
'''

print(len(programs_list), len(set(programs_list)))
print(programs_list[1000000000%count])
