# little helper class that parses game data on instantiation and has a helper
# method that calculates the power of the minimum set of the game
class Game:
    def __init__(self, game_row):
        # start by setting max values to zero, we will increase them as we
        # add the sets
        self.max_red = 0
        self.max_blue = 0
        self.max_green = 0

        # pull out the game id with simple (kind of tedious though) string parsing
        game_data = game_row.split(': ')
        self.game_id = int(game_data[0].split(' ')[-1])

        # parse the sets and then add them one by one
        game_sets = game_data[1].split('; ')
        for game_set in game_sets:
            self.add_set(game_set)

    # helper function to add a set from the game
    def add_set(self, incoming_set):
        colours = incoming_set.split(', ')
        for colour in colours:
            # more string parsing to get to our data
            colour = colour.split(' ')
            amount = int(colour[0])
            colour = colour[1]

            # we only really care about maximums, so that's all that we'll check
            # for and keep track of
            if (colour == 'red' and amount > self.max_red):
                self.max_red = amount
            elif (colour == 'blue' and amount > self.max_blue):
                self.max_blue = amount
            if (colour == 'green' and amount > self.max_green):
                self.max_green = amount

    # as defined in the problem, the power is calculated by taking the minumum
    # necessary number of red, green, and blue and multiplying the three together.
    # this minimum necessary is the same as the max count that we've kept track of.
    def get_power(self):
        return self.max_red * self.max_green * self.max_blue

# take the game history data and parse it into Game objects
with open("input.txt") as game_history_data:
    games = [Game(row.strip()) for row in game_history_data]

# loop through games and keep track of the IDs of ones that are possible
powers = []
for game in games:
    powers.append(game.get_power())

# finally, print the sum of the valid game IDs
print(sum(powers))

