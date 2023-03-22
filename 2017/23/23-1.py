from collections import Counter
import itertools

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
mul_count = 0

with open("input.txt") as instructions_list:
    instructions = [rows.split() for rows in instructions_list]

while i < len(instructions):
    print(registers)

    instruction = instructions[i]

    if instruction[0] == "set":
        registers[instruction[1]] = get_val(registers, instruction[2])
    elif instruction[0] == "sub":
        registers[instruction[1]] = get_val(registers, instruction[1]) - get_val(registers, instruction[2])
    elif instruction[0] == "mul":
        registers[instruction[1]] = get_val(registers, instruction[1]) * get_val(registers, instruction[2])
        mul_count += 1
    elif instruction[0] == "jnz":
        if (get_val(registers, instruction[1]) != 0):
            i += int(instruction[2])
            continue

    i += 1

print(mul_count)
