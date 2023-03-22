def how_many_steps():
    count = 0
    location = 0

    with open("input.txt") as list:
        steps = list.read().splitlines()

    while location < len(steps):
        current_jump = int(steps[location])
        steps[location] = current_jump + 1
        location = location + current_jump
        count = count + 1

    return count


how_many_steps()
