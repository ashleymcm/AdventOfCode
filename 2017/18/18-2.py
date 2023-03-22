from collections import Counter
import os, sys, itertools

def is_int(val):
  try:
    int(val)
    return True
  except ValueError:
    return False

def get_val(registers, val, p):
    if is_int(val):
        return int(val)
    if val not in registers:
        if val == "p":
            registers[val] = p
        else:
            registers[val] = 0
    return registers[val]

registers = {}
registers2 = {}
send = []
send2 = []
count = 0


dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
with open(os.path.join(dirname, "input.txt")) as instructions_list:
    instructions = [rows.split() for rows in instructions_list]

i = 0
j = 0

while True:
    p = 0

    while i < len(instructions):
        instruction = instructions[i]

        if instruction[0] == "snd":
            send.append(get_val(registers, instruction[1], p))
        elif instruction[0] == "set":
            registers[instruction[1]] = get_val(registers, instruction[2], p)
        elif instruction[0] == "add":
            registers[instruction[1]] = get_val(registers, instruction[1], p) + get_val(registers, instruction[2], p)
        elif instruction[0] == "mul":
            registers[instruction[1]] = get_val(registers, instruction[1], p) * get_val(registers, instruction[2], p)
        elif instruction[0] == "mod":
            registers[instruction[1]] = get_val(registers, instruction[1], p) % get_val(registers, instruction[2], p)
        elif instruction[0] == "rcv":
            if len(send2) > 0:
                registers[instruction[1]] = send2[0]
                del send2[0]
            else:
                break
        elif instruction[0] == "jgz":
            if (get_val(registers, instruction[1], p) > 0):
                i += get_val(registers, instruction[2], p)
                continue
        i += 1

    p = 1

    while j < len(instructions):
        instruction = instructions[j]

        if instruction[0] == "snd":
            send2.append(get_val(registers2, instruction[1], p))
            count += 1
        elif instruction[0] == "set":
            registers2[instruction[1]] = get_val(registers2, instruction[2], p)
        elif instruction[0] == "add":
            registers2[instruction[1]] = get_val(registers2, instruction[1], p) + get_val(registers2, instruction[2], p)
        elif instruction[0] == "mul":
            registers2[instruction[1]] = get_val(registers2, instruction[1], p) * get_val(registers2, instruction[2], p)
        elif instruction[0] == "mod":
            registers2[instruction[1]] = get_val(registers2, instruction[1], p) % get_val(registers2, instruction[2], p)
        elif instruction[0] == "rcv":
            if len(send) > 0:
                registers2[instruction[1]] = send[0]
                del send[0]
            else:
                break
        elif instruction[0] == "jgz":
            if (get_val(registers2, instruction[1], p) > 0):
                j += get_val(registers2, instruction[2], p)
                continue
        j += 1

    if len(send) == 0 and len(send2) == 0:
        break;

print(count)
