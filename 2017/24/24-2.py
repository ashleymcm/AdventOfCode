from collections import Counter
import os, sys, itertools

def find_component(components, number):
    contains = []
    for component in components:
        if number in component:
            contains.append(component)
    return contains

def make_bridges(number, components, bridge, bridges):
    for component in components:
        new_bridge = list(bridge)
        new_bridge.append(component)
        if number == component[0]:
            new_comps = list(components)
            new_comps.remove(component)
            make_bridges(component[1], new_comps, new_bridge, bridges)
        elif number == component[1]:
            new_comps = list(components)
            new_comps.remove(component)
            make_bridges(component[0], new_comps, new_bridge, bridges)

    bridges.append(bridge)

    return bridges

def get_bridge_strength(bridge):
    strength = 0
    for component in bridge:
        strength += sum(component)
    return strength

def get_max_bridge_strength(bridges):
    max_strength = 0
    for bridge in bridges:
        strength = get_bridge_strength(bridge)
        if strength > max_strength:
            max_strength = strength
    return max_strength

def get_longest_bridges(bridges):
    longest_length = 0
    long_bridges = []
    for bridge in bridges:
        if len(bridge) > longest_length:
            longest_length = len(bridge)
            long_bridges = [bridge]
        elif len(bridge) == longest_length:
            long_bridges.append(bridge)
    return long_bridges

# get all pieces from input
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
with open(os.path.join(dirname, "input.txt")) as grid:
    components = [sorted(map(int, row.strip().split("/"))) for row in grid]

# sort components based on first of pair (makes comparisons easier later)
components = sorted(components, key=lambda x: (x[0], x[1]))
bridges = []

# get starters
starters = [component for component in components if component[0] == 0]
bridges = []
for starter in starters:
    new_comps = list(components)
    new_comps.remove(starter)
    bridges += make_bridges(starter[1], new_comps, [starter], [])


print(get_max_bridge_strength(get_longest_bridges(bridges)))
