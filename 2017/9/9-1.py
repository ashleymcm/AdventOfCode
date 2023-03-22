import re


def remove_garbage(stream):
    stream = re.sub(r"!.", "", stream)
    stream = re.sub(r"<(.*?)>", "", stream)
    return stream


current_weight = 0
score = 0

with open("input.txt") as file:
    stream = file.read()

# remove garbage
stream = remove_garbage(stream)

# loop through characters in stream
for char in stream:
    if char == '{':
        current_weight = current_weight + 1
        score += current_weight
    elif char == '}':
        current_weight = current_weight - 1

print(score)
