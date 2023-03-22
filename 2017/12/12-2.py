import itertools


class Program:

    def __init__(self, id, links):
        self.id = id
        self.links = links


def find_all_in_group(group_id, programs, group):

    program = [x for x in programs if x.id == group_id][0]

    for link in program.links:
        if link not in group:
            group.add(link)
            group.union(find_all_in_group(link, programs, group))
    return group


def find_num_groups():
    all_programs = set()
    group_count = 0

    with open("input.txt") as list:
        programs = [programs.split() for programs in list]

    for i in range(len(programs)):
        id = int(programs[i][0])
        all_programs.add(id)
        links = [int(link.replace(",", "")) for link in programs[i][2: len(programs[i])]]
        programs[i] = Program(id, links)

    while len(all_programs) > 0:
        next_program = next(iter(all_programs))
        group = find_all_in_group(next_program, programs, set())
        all_programs = all_programs.difference(group)
        group_count += 1

    return group_count


print(find_num_groups())
