from collections import Counter
import os, sys, itertools

def is_int(val):
  try:
    int(val)
    return True
  except ValueError:
    return False

def get_val(registers, val):
    if is_int(val):
        return int(val)
    if val not in registers:
        registers[val] = 0
    return registers[val]

registers = {}
sound = 0
i = 0

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
with open(os.path.join(dirname, "input.txt")) as instructions_list:
    instructions = [rows.split() for rows in instructions_list]

while i < len(instructions):
    instruction = instructions[i]

    if instruction[0] == "snd":
        sound = get_val(registers, instruction[1])
    elif instruction[0] == "set":
        registers[instruction[1]] = get_val(registers, instruction[2])
    elif instruction[0] == "add":
        registers[instruction[1]] = get_val(registers, instruction[1]) + get_val(registers, instruction[2])
    elif instruction[0] == "mul":
        registers[instruction[1]] = get_val(registers, instruction[1]) * get_val(registers, instruction[2])
    elif instruction[0] == "mod":
        registers[instruction[1]] = get_val(registers, instruction[1]) % get_val(registers, instruction[2])
    elif instruction[0] == "rcv":
        if (get_val(registers, instruction[1]) > 0):
            print(sound)
            break
    elif instruction[0] == "jgz":
        if (get_val(registers, instruction[1]) > 0):
            i += get_val(registers, instruction[2])
            continue

    i += 1
