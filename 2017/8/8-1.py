from collections import Counter
import os, sys, itertools

def perform_update(register, action, amount, conditional_register, conditional_compare, conditional_number, registers):

    if conditional_register not in registers:
        registers[conditional_register] = 0

    if register not in registers:
        registers[register] = 0

    if conditional_compare == "==":
        if registers[conditional_register] == conditional_number:
            return perform_action(register, action, amount, registers)

    elif conditional_compare == "!=":
        if registers[conditional_register] != conditional_number:
            return perform_action(register, action, amount, registers)

    elif conditional_compare == ">=":
        if registers[conditional_register] >= conditional_number:
            return perform_action(register, action, amount, registers)

    elif conditional_compare == "<=":
        if registers[conditional_register] <= conditional_number:
            return perform_action(register, action, amount, registers)

    elif conditional_compare == ">":
        if registers[conditional_register] > conditional_number:
            return perform_action(register, action, amount, registers)

    elif conditional_compare == "<":
        if registers[conditional_register] < conditional_number:
            return perform_action(register, action, amount, registers)

    return registers


def perform_action(register, action, amount, registers):
    if action == "inc":
        registers[register] += amount

    elif action == "dec":
        registers[register] -= amount

    return registers


dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
registers = dict()
max_ever = 0

# take the list of banks and turn it into an int array
with open(os.path.join(dirname, "input.txt")) as instructions_list:
    instructions = [instructions.split() for instructions in instructions_list]

for instruction in instructions:
    registers = perform_update(instruction[0], instruction[1], int(instruction[2]), instruction[4], instruction[5], int(instruction[6]), registers)
    if max(registers.values()) > max_ever:
        max_ever = max(registers.values())

print(max(registers.values()))
print(max_ever)
