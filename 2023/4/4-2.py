# little helper class that parses card data on instantiation.
# i seem to really be feeling classes this year?
class Card:
    def __init__(self, card_row):
        # pull out the card id
        card_data = card_row.split(': ')
        self.card_id = int(card_data[0].split(' ')[-1])

        # parse the number sets and store them as actual sets
        all_numbers = card_data[1].split('| ')
        self.winning_numbers = set(all_numbers[0].strip().split())
        self.card_numbers = set(all_numbers[1].strip().split())

        # now calculate and store number of matches
        intersection = self.winning_numbers & self.card_numbers
        self.num_matches = len(intersection)

# take the card data and parse it into Card objects
with open("input.txt") as card_data:
    cards = [Card(row.strip()) for row in card_data]

# initialize the card_count dictionary with one card of each id, the "originals"
card_count = {}
for card in cards:
    card_count[card.card_id] = 1

# loop through cards to make copies based on how many matches the current card has
for card in cards:
    number_of_cards = card_count[card.card_id]

    for i in range(card.num_matches):
        # loop through according to instructions where for every match found on this
        # card a new card is created in series
        next_card_num = card.card_id + i + 1
        card_count[next_card_num] += number_of_cards

# finally, print the sum
print(sum(card_count.values()))