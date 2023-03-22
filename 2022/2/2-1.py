import os, sys
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

points_map = {
  'X': 1,
  'Y': 2,
  'Z': 3
}

def roundWon(round):
  if (
       (round[0] == 'A' and round[1] == 'Y') or
       (round[0] == 'B' and round[1] == 'Z') or
       (round[0] == 'C' and round[1] == 'X')
    ):
    return True
  return False

def roundDraw(round):
  if (
       (round[0] == 'A' and round[1] == 'X') or
       (round[0] == 'B' and round[1] == 'Y') or
       (round[0] == 'C' and round[1] == 'Z')
    ):
    return True
  return False

def calculatePoints(rounds):
  total = 0
  for round in rounds:
    if (roundWon(round)):
      total += 6
    elif (roundDraw(round)):
      total += 3
    total += points_map[round[1]]
  return total

with open(os.path.join(dirname, "input.txt")) as rounds_list:
  rounds = [rounds.split(" ") for rounds in rounds_list.read().split("\n")]
  print(calculatePoints(rounds))