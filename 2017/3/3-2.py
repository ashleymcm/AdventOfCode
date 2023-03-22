import math

# i feel like there is a more elegant solution but i lost patience and it's my weekend
# so i just more-or-less brute-forced this mofo. warning: extremely inefficient code ahead!

# brought over my PerfectSquarePoint class from 3-1 and also encapsulated most of the rest
# of the logic from that one into Square: with Square I can create an object that will hold
# and calculate the cell's position, value, and x,y coordinates, not to mention loop through
# the array of squares to find all the "neighbours". there's really no reason i should be
# passing the array of squares in to make a new square, i kind of just got tired once it was
# working and stopped. i'll probably go back and at least make it *look* more elegant, even if
# it's not very elegant at its core.


class PerfectSquarePoint:

    def __init__(self, root):
        self.root = root
        self.half_root = math.floor(root/2)
        self.square = root*root
        self.even = self.square % 2 == 0
        self.x = self.get_x()
        self.y = self.get_y()

    def get_x(self):
        if self.even:
            return 1 - self.half_root
        else:
            return self.half_root

    def get_y(self):
        if self.even:
            return -self.half_root
        else:
            return self.half_root


class Square:
    def __init__(self, position, squares):
        self.position = position
        self.squares = squares
        self.root = math.sqrt(position)

        self.lesser_perfect_square_root = int(self.root)
        self.greater_perfect_square_root = self.lesser_perfect_square_root + 1

        self.lesser_square = PerfectSquarePoint(self.lesser_perfect_square_root)
        self.greater_square = PerfectSquarePoint(self.greater_perfect_square_root)

        self.difference_from_lesser = position - self.lesser_square.square
        self.difference_from_greater = self.greater_square.square - position

        self.x = self.find_x()
        self.y = self.find_y()
        self.value = self.calculate_value()

    def find_x(self):
        if self.root.is_integer():
            point = PerfectSquarePoint(self.root)
            return point.x

        if self.lesser_square.even and not self.greater_square.even:
            if (self.difference_from_lesser <= self.greater_square.root):
                return self.lesser_square.x - 1
            else:
                return self.greater_square.x - self.difference_from_greater
        elif not self.lesser_square.even and self.greater_square.even:
            if (self.difference_from_lesser <= self.greater_square.root):
                return self.lesser_square.x + 1
            else:
                return self.greater_square.x + self.difference_from_greater

    def find_y(self):
        if self.root.is_integer():
            point = PerfectSquarePoint(self.root)
            return point.y

        if self.lesser_square.even and not self.greater_square.even:
            if (self.difference_from_lesser <= self.greater_square.root):
                return self.lesser_square.y - 1 + self.difference_from_lesser
            else:
                return self.greater_square.y
        elif not self.lesser_square.even and self.greater_square.even:
            if (self.difference_from_lesser <= self.greater_square.root):
                return self.lesser_square.y + 1 - self.difference_from_lesser
            else:
                return self.greater_square.y

    def is_a_neighbour(self, square):
        x_is_less_than_one_away = self.is_one_or_less_away(self.x, square.x)
        y_is_less_than_one_away = self.is_one_or_less_away(self.y, square.y)

        return x_is_less_than_one_away and y_is_less_than_one_away

    def is_one_or_less_away(self, x1, x2):
        return abs(x1 - x2) <= 1

    def calculate_value(self):
        if len(self.squares) < 2:
            return 1

        value = 0
        neighbours = [square for square in self.squares if self.is_a_neighbour(square)]
        for neighbour in neighbours:
            value += neighbour.value

        return value


# simply looping through and making a new square when the value of the last one isn't
# greater than our input is all it takes to run the code since everything is done in
# the objects above

def find_first_value_greater_than(value):
    # this is really just a do-while
    squares = []
    squares.append(Square(1, squares))

    while squares[-1].value < value:
        last_square = squares[-1]
        squares.append(Square(last_square.position + 1, squares))

    return squares[-1].value


# easy part of just calling the method (:
find_first_value_greater_than(361527)
