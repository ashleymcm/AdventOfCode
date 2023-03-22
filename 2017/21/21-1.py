import os, sys, math

def count_items(images):
    count = 0
    for image in images:
        for char in image:
            if char == '#':
                count += 1
    return count

def flip_h(image):
    flipped = []
    for row in image:
        flipped.append(list(reversed(row)))
    return flipped

def flip_v(image):
    flipped = []
    index = len(image) - 1
    while index >= 0:
        flipped.append(image[index])
        index -= 1
    return flipped

def rotate(image):
    rotated = []
    for i in range(len(image)):
        row = []
        index = len(image) - 1
        while index >= 0:
            #print(image)
            #print(index, i)
            row.append(image[index][i])
            index -= 1
        rotated.append(row)
    return rotated

def break_apart(image):
    if len(image) == 2 or len(image) == 3:
        return image
    else:
        size = 2
        images = []
        if len(image) % 2 != 0:
            size = 3
        j = 0
        while j < len(image):
            i = 0
            while i < len(image[j]):
                img = []
                for k in range(size):
                    img.append(image[j + k][i: i + size])
                images.append(img)
                i += size
            j += size

    return images

def put_together(images):
    image = []
    length = 0
    if len(images) == 1:
        return images
    elif len(images) % 3 == 0:
        length = len(images)/3
    else:
        length = len(images)/2

    i = 0
    while i < len(images):
        for j in range(len(images[0])):
            row = []
            for k in range(length):
                row += images[i + k][j]
            image.append(row)
        i += length

    return image

def find_match(image, rules):
    for rule in rules:
        if len(image) == len(rule[0]):
            if image == rule[0] or flip_h(image) == rule[0] or flip_v(image) == rule[0] or flip_v(flip_h(image)) == rule[0]:
                return rule[1]
            if rotate(image) == rule[0] or rotate(flip_h(image)) == rule[0] or rotate(flip_v(image)) == rule[0] or rotate(flip_v(flip_h(image))) == rule[0]:
                return rule[1]
            if rotate(rotate(image)) == rule[0] or rotate(rotate(flip_h(image))) == rule[0] or rotate(rotate(flip_v(image))) == rule[0] or rotate(rotate(flip_v(flip_h(image)))) == rule[0]:
                return rule[1]
            if rotate(rotate(rotate(image))) == rule[0] or rotate(rotate(rotate(flip_h(image)))) == rule[0] or rotate(rotate(rotate(flip_v(image)))) == rule[0] or rotate(rotate(rotate(flip_v(flip_h(image))))) == rule[0]:
                return rule[1]
    return image


dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
with open(os.path.join(dirname, "input.txt")) as grid:
    rows = [row.strip().split(" => ") for row in grid]

rules = []



for i in range(len(rows)):
    rule_0 = [list(rule) for rule in rows[i][0].split('/')]
    rule_1 = [list(rule) for rule in rows[i][1].split('/')]

    rule = [rule_0, rule_1]
    rules.append(rule)
#print(rules)
image = [[".","#","."], [".",".","#"], ["#","#","#"]]

for i in range(5):
    if len(image) > 3:
        #print(image)
        images = break_apart(image)
        #print(images)
        for i in range(len(images)):
            images[i] = find_match(images[i], rules)
        #print(images)
        image = put_together(images)
        #print(image)
    else:
        image = find_match(image, rules)
    #print(" ")
print(count_items(image))
