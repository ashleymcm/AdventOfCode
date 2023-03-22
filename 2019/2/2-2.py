import os, sys, math

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

##loop through input row, or "ints"
with open(os.path.join(dirname, "input.txt")) as ints_list:
    ints = [int(x) for x in [ints.split(",") for ints in ints_list][0]]

def freshInput():
    return ints.copy()

memory = freshInput()
correct_output = 19690720

def prepInput(noun, verb):
    memory[1] = noun
    memory[2] = verb

def calcAnswer(noun, verb):
    return noun * 100 + verb

def performAction(address):
    if memory[address] == 1:
        memory[memory[address + 3]] = memory[memory[address + 1]] + memory[memory[address + 2]]
    elif memory[address] == 2:
        memory[memory[address + 3]] = memory[memory[address + 1]] * memory[memory[address + 2]]

def run():
    address = 0
    while (memory[address] != 99):
        performAction(address)
        address += 4

def findNounAndVerb():
    global memory
    for noun in range(100):
        for verb in range(100):
            memory = freshInput()
            prepInput(noun, verb)
            run()
            if (memory[0] == correct_output):
                return calcAnswer(noun, verb)

print(findNounAndVerb())
