import os, sys
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

def formatCrates(crates):
  crates_list = crates.split("\n")
  crates_list.reverse()
  crates_list.pop(0)
  formatted_crates = list()
  for crate_string in crates_list:
    crate_num = 0
    for i in range(len(crate_string))[1::4]:
      if crate_string[i] != " ":
        if len(formatted_crates) <= crate_num:
          formatted_crates.append(crate_string[i])
        else:
          formatted_crates[crate_num] += crate_string[i]
      crate_num += 1
  return formatted_crates

def formatMoves(moves):
  moves_list = moves.split("\n")
  formatted_moves = list()
  for move in moves_list:
    chars = move.split(" ")
    formatted_move = list()
    for char in chars:
      if char.isdigit():
        formatted_move.append(int(char))
    formatted_moves.append(formatted_move)

  return formatted_moves

def performMove(crates, move):
  num_crates, from_stack, to_stack = move[0], move[1] - 1, move[2] - 1
  crates_to_move = crates[from_stack][-num_crates:]
  crates[from_stack] = crates[from_stack][0:len(crates[from_stack]) - num_crates]
  crates[to_stack] += crates_to_move
  return crates

def moveCrates(crates, moves):
  for move in moves:
    crates = performMove(crates, move)
  return crates

def findTopCratesAfterMove(crates, moves):
  crates = moveCrates(crates, moves)
  top_crates = ""
  for crate in crates:
    top_crates += crate[-1:]
  return top_crates

with open(os.path.join(dirname, "input.txt")) as crate_data:
  crate_data = crate_data.read().split("\n\n")
  crates = formatCrates(crate_data[0])
  moves = formatMoves(crate_data[1])
  print(findTopCratesAfterMove(crates, moves))