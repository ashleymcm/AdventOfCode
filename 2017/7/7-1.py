import numpy as np

class Program:

    def __init__(self, name, weight, subprograms):
        self.name = name
        self.weight = weight
        self.subprograms = subprograms


def bottom_program():
    names = []
    all_subprograms = []

    with open("input.txt") as list:
        programs = [programs.split() for programs in list]

    for i in range(len(programs)):
        name = programs[i][0]
        names.append(name)

        weight = int(programs[i][1].replace("(", "").replace(")", ""))

        subprograms = [subprogram.replace(",", "") for subprogram in programs[i][3: len(programs[i])]]
        all_subprograms = all_subprograms + subprograms

        programs[i] = Program(name, weight, subprograms)

    base_programs = np.setdiff1d(names, all_subprograms)

    return base_programs[0]


print(bottom_program())
