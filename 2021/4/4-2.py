import os, sys

# i hate that i need this when i'm on my windows machine
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

# turn the rows in cols and vice versa - this is to prep our search
# for later and hopefully save some time/effort
def flipCard(card):
	flipped_card = [[] for i in range(len(card))]

	for x in range(0, len(card)):
		for y in range(0, len(card)):
			flipped_card[x].append(card[y][x])

	return flipped_card

# check if the card has bingo, i.e. if any of its rows have all numbers
# in the selected numbers
def cardHasBingo(card, selected_numbers):
	for row in card:
		if all(x in selected_numbers for x in row):
			return True
	
	return False

# loop through selected numbers and cards until i find the last one that
# has a bingo. return its index and the numbers that have been selected
def findLastBingo(numbers, cards, cards_flipped):
	
  numbers_index = 5 # need at least 5 numbers to get a bingo so start at 4
  unfound_bingos = list(range(0, len(cards)))
  last_found = None

  while len(unfound_bingos) > 0:
    selected_numbers = numbers[:numbers_index]
		
		# it's nice and easy to look for bingos because we already have our data
		# organized to have both rows AND columns (via our flipped cards) as rows in lists
    for i in unfound_bingos:
      if cardHasBingo(cards[i], selected_numbers):
        unfound_bingos.remove(i) # when a card is found, remove it from the list so that
        last_found = i           # we don't search it anymore - save it so we can return 
        continue	               # the index of the very last one
      elif cardHasBingo(cards_flipped[i], selected_numbers):
        unfound_bingos.remove(i)
        last_found = i
        continue

    numbers_index += 1

  # almost the same return as the last question, but we reduce the number index for the
  # selected numbers because we incremented it an extra, unnecessary time before ending 
  # the loop above
  return last_found, numbers[:numbers_index - 1]

# calculate the score the way it told me to - add up any _uncalled_ numbers and them
# multiply it by the last called number, for reasons 
def calculateScore(cards, card_index, selected_numbers):
	card = cards[card_index]
	card_sum = 0

	for x in range(0, len(card)):
		for y in range(0, len(card)):
			if card[x][y] not in selected_numbers:
				card_sum += int(card[x][y])

	return card_sum * int(selected_numbers[-1])

# read data and first separate by empty newline, or \n\n
with open(os.path.join(dirname, "input.txt")) as input_data:
  data = input_data.read().split('\n\n')

# the first line is a comma-separated list of numbers, so let's grab those
numbers = data.pop(0).rstrip().lstrip().split(',')

# the rest of the data are the cards, so let's first split them into proper rows 
# and then a full-on 2D array, or list of lists
cards = [card.split('\n') for card in data]
cards = [[row.split() for row in card] for card in cards]

# take the cards above and flip them, turning rows into columns so that it's easier
# to look for bingos
cards_flipped = [flipCard(card) for card in cards]

# find the first bingo
card_index, selected_numbers = findLastBingo(numbers, cards, cards_flipped)

# print the score
print(calculateScore(cards, card_index, selected_numbers))