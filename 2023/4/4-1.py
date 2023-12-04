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

        # now calculate scores
        intersection = self.winning_numbers & self.card_numbers
        if (len(intersection) == 0):
            self.score = 0
        else:
            # we get 1 point for the first match, and then it's doubled
            # (i.e. multiplied by 2) for each point after, so we can use
            # exponents with base 2
            self.score = 2 ** (len(intersection) - 1)

# take the card data and parse it into Card objects
with open("input.txt") as card_data:
    cards = [Card(row.strip()) for row in card_data]

# loop through cards and add each card's score to the total sum
score_sum = 0
for card in cards:
    score_sum += card.score

# finally, print the sum
print(score_sum)