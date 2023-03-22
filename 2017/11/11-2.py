from collections import Counter
import os, sys, itertools

def do_cancellation(x, y):
    if x >= y:
        x = x - y
        y = 0
    elif y > x:
        y = y - x
        x = 0

    return x, y

def do_cancellations(n, s, ne, nw, se, sw):
    n, s = do_cancellation(n, s)
    ne, sw = do_cancellation(ne, sw)
    nw, se = do_cancellation(nw, se)

    return n, s, ne, nw, se, sw

def do_half_cancellation(x, y, z, anti_y):
    if x >= z:
        y = y + z
        x = x - z
        z = 0
    elif z > x:
        y = y + x
        z = z - x
        x = 0

    y, anti_y = do_cancellation(y, anti_y)

    return x, y, z, anti_y

def minimum_distance(steps):
    n = 0
    s = 0
    ne = 0
    se = 0
    sw = 0
    nw = 0

    n = steps.count('n')
    s = steps.count('s')
    ne = steps.count('ne')
    nw = steps.count('nw')
    se = steps.count('se')
    sw = steps.count('sw')

    n, s, ne, nw, se, sw = do_cancellations(n, s, ne, nw, se, sw)

    n, ne, se, sw = do_half_cancellation(n, ne, se, sw)
    ne, se, s, nw = do_half_cancellation(ne, se, s, nw)
    se, s, sw, n = do_half_cancellation(se, s, sw, n)
    s, sw, nw, ne = do_half_cancellation(s, sw, nw, ne)
    sw, nw, n, se = do_half_cancellation(sw, nw, n, se)
    nw, n, ne, s = do_half_cancellation(nw, n, ne, s)

    return n + s + ne + nw + se + sw

def farthest_distance():
    distances = []
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

    with open(os.path.join(dirname, "input.txt")) as steps_list:
        steps = steps_list.read().strip().split(",")

    for i in range(len(steps)):
        current_path = steps[0:i]
        distances.append(minimum_distance(current_path))

    return max(distances)


print(farthest_distance())
