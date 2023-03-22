from collections import deque

def move_left(arr, index):
    if index <= 0:
        arr.appendleft(0)
        return arr, 0
    else:
        return arr, index - 1

def move_right(arr, index):
    if index >= len(arr) - 1:
        arr.append(0)
    return arr, index + 1

def do_action(arr, index, new_value, direction):
    arr[index] = new_value
    if direction > 0:
        return move_right(arr, index)
    else:
        return move_left(arr, index)

A = [1, 1, "B", 0, 0, "E"]
B = [1, 0, "C", 0, 1, "A"]
C = [1, 0, "D", 0, 1, "C"]
D = [1, 0, "E", 0, 0, "F"]
E = [1, 0, "A", 1, 0, "C"]
F = [1, 0, "E", 1, 1, "A"]



def get_checksum(arr):
    return arr.count(1)

index = 0
count = 0
arr = deque()
arr.append(0)
current_state = A

while count < 12208951:
    if arr[index] == 0:
        arr, index = do_action(arr, index, current_state[0], current_state[1])
        current_state = eval(current_state[2])
    else:
        arr, index = do_action(arr, index, current_state[3], current_state[4])
        current_state = eval(current_state[5])
    count += 1

print(get_checksum(arr))
