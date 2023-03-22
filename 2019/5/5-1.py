import os, sys, math

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

##loop through input row, or "ints"
with open(os.path.join(dirname, "input.txt")) as ints_list:
    ints = [int(x) for x in [ints.split(",") for ints in ints_list][0]]

memory = ints

def getParam(mode, param):
    if mode == '0':
        return memory[param]
    elif mode == '1':
        return param

def getOp(code):
    return int(code[-2:])

def getParamTypes(code):
    substr = code [:-2]
    return substr[::-1]

def performActionAndReturnPointerDifference(op, address, paramTypes):
    print(op, address, paramTypes)
    if op == 1:
        memory[getParam(paramTypes[2], address + 3)] = memory[getParam(paramTypes[0], address + 1)] + memory[getParam(paramTypes[1], address + 2)]
        return 4
    elif op == 2:
        memory[getParam(paramTypes[2], address + 3)] = memory[getParam(paramTypes[0], address + 1)] * memory[getParam(paramTypes[1], address + 2)]
        return 4
    elif op == 3:
        memory[getParam(paramTypes[0], address + 1)] = 1
        return 2
    elif op == 4:
        print(memory[getParam(paramTypes[0], address + 1)])
        return 2

def run():
    address = 0
    code = str(memory[address]).rjust(5, '0')
    print(code)
    op = getOp(code)
    paramTypes = getParamTypes(code)
    while (op != 99):
        code = str(memory[address]).rjust(5, '0')
        print(code)
        op = getOp(code)
        paramTypes = getParamTypes(code)
        address += performActionAndReturnPointerDifference(op, address, paramTypes)

run()
