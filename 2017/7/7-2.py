import numpy as np

class Program:

    def __init__(self, name, weight, subprograms):
        self.name = name
        self.weight = weight
        self.subprograms = subprograms


def get_program_by_name(program_name, programs):
    return next((x for x in programs if x.name == program_name), None)


def balance():
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

    for program in programs:
        total_weight(program, programs)


def total_weight(program, programs):
    weight = program.weight
    weights = []

    for sub in program.subprograms:
        sub_program = get_program_by_name(sub, programs)
        if len(sub_program.subprograms) > 0:
            totalweight = total_weight(sub_program, programs)
            weights.append(totalweight)
            weight += totalweight
        else:
            weight += sub_program.weight

    for i in range(len(weights) - 1):
        w = weights[i]
        if weights.count(w) == 1:
            print(weights, w)
            if i == len(weights):
                correct_imbalance(program.subprograms[i], programs, weights[0])
            else:
                correct_imbalance(program.subprograms[i], programs, weights[i + 1])
    return weight


def correct_imbalance(program_name, programs, desired_weight):
    program = get_program_by_name(program_name, programs)
    is_sub_weight = False
    weight = program.weight
    weights = []

    for sub in program.subprograms:
        sub_program = get_program_by_name(sub, programs)
        weights.append(total_weight(sub_program, programs))

    for i in range(len(weights) - 1):
        w = weights[i]
        if weights.count(w) == 1:
            if i == len(weights):
                print(weights[i])
                is_sub_weight = True
            else:
                print(weights[i + 1])
                is_sub_weight = True

    if not is_sub_weight:
        print(desired_weight - sum(weights))


balance()
