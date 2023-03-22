import os, sys
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

points_map = {
  'A': 1,
  'B': 2,
  'C': 3
}

rules_map = {
  'A': {
    'win': 'C',
    'lose': 'B',
    'draw': 'A'
  },
  'B': {
    'win': 'A',
    'lose': 'C',
    'draw': 'B'
  },
  'C': {
    'win': 'B',
    'lose': 'A',
    'draw': 'C'
  },
}

def calculatePoints(rounds):
  total = 0
  for round in rounds:
    if (round[1] == 'X'): #lose, so other player must win
      option_to_choose = rules_map[round[0]]['win']
      total += points_map[option_to_choose]
    elif (round[1] == 'Y'): #draw
      total += 3
      option_to_choose = rules_map[round[0]]['draw']
      total += points_map[option_to_choose]
    elif (round[1] == 'Z'): #win, so other player must lose
      total += 6
      option_to_choose = rules_map[round[0]]['lose']
      total += points_map[option_to_choose]
  return total

with open(os.path.join(dirname, "input.txt")) as rounds_list:
  rounds = [rounds.split(" ") for rounds in rounds_list.read().split("\n")]
  print(calculatePoints(rounds))