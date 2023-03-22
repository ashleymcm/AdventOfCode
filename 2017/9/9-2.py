import re


def count_garbage(stream):
    garbage_sum = 0

    stream = re.sub(r"!.", "", stream)
    garbage_areas = re.findall(r"<(.*?)>", stream)
    for garbage in garbage_areas:
        garbage_sum += len(garbage)

    print(garbage_sum)


with open("input.txt") as file:
    stream = file.read()

# count garbage
count_garbage(stream)
