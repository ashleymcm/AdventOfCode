import os, sys, itertools
from collections import Counter

##small method to generate the intersection of two strings
def intersection(s1, s2):
  out = ""
  for i in range(len(s1)):
    if s1[i] == s2[i]:
      out += s1[i]
  return out

  
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

##loop through input rows, or "box IDs"
with open(os.path.join(dirname, "input.txt")) as box_id_list:
    box_ids = [box_ids.split() for box_ids in box_id_list]

##get the length of an ID -- they are all the same
length = len(box_ids[0][0])

##compare each box ID with each other once
for a, b in itertools.combinations(box_ids, 2):
    ##find the intersection of the two IDs
    c = intersection(a[0], b[0])

    ##if the length of the intersection is one less than the length of an ID we have a match
    if len(c) == length - 1:
        print(c)


