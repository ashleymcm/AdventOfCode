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


with open("input.txt") as list:
    programs = [programs.split() for programs in list]

for i in range(len(programs)):
    id = int(programs[i][0])
    links = [int(link.replace(",", "")) for link in programs[i][2: len(programs[i])]]
    programs[i] = Program(id, links)

group = set()

print(len(find_all_in_group(0, programs, group)))
