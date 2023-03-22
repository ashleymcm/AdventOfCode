import math

# incoming shitty brain dump:
#
# it seems that every odd perfect square forms the bottom-right base of a spiral
# (makes a diagonal from 1 down through the base of the square)
# whereas the even perfect squares make a parallel line going in the up-left direction
# to the right of the top-left corner. this gives a base "formula"
# of odd square = (x, x) and even square = (1-x, -x) where 1 is at the origin (0, 0)
# and x = the ceiling of sqrt(num)/2
# we can make a lil class to hold & calculate this info so that the code is less awful


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


def calculate_num_steps(square):
    # first let's test to see if our number is a perfect square, because that saves
    # us a bunch of trouble
    root = math.sqrt(square)
    if root.is_integer():
        point = PerfectSquarePoint(root)
        return calculate_distance_from_coordinates(point.x, point.y)

    # obviously if we got this far it's not a perfect square and we do this
    # the long way...

    # find the two perfect squares that square rests between
    lesser_perfect_square_root = int(math.sqrt(square))
    greater_perfect_square_root = lesser_perfect_square_root + 1

    # make a PerfectSquarePoint for each, for ease of calculations later
    lesser_square = PerfectSquarePoint(lesser_perfect_square_root)
    greater_square = PerfectSquarePoint(greater_perfect_square_root)

    # get differences between squares to calculate coordinates
    difference_from_lesser = square - lesser_square.square
    difference_from_greater = greater_square.square - square

    # calculate coordinates
    square_x = find_x(lesser_square, greater_square, difference_from_lesser, difference_from_greater)
    square_y = find_y(lesser_square, greater_square, difference_from_lesser, difference_from_greater)
    return (calculate_distance_from_coordinates(square_x, square_y))

# calculating the coordinates is the tricky part:
#
# we can use the data of the bookending perfect squares being even or odd in addition to
# the difference between the given number and the smaller of the perfect squares to determine
# which "arm" of the spiral the number is on and move coordinates accordingly. those calculations
# are done in the two methods directly below.


def find_x(lesser_square, greater_square, difference_from_lesser, difference_from_greater):
    if lesser_square.even and not greater_square.even:
        if (difference_from_lesser <= greater_square.root):
            return lesser_square.x - 1
        else:
            return greater_square.x - difference_from_greater
    elif not lesser_square.even and greater_square.even:
        if (difference_from_lesser <= greater_square.root):
            return lesser_square.x + 1
        else:
            return greater_square.x + difference_from_greater


def find_y(lesser_square, greater_square, difference_from_lesser, difference_from_greater):
    if lesser_square.even and not greater_square.even:
        if (difference_from_lesser <= greater_square.root):
            return lesser_square.y - 1 + difference_from_lesser
        else:
            return greater_square.y
    elif not lesser_square.even and greater_square.even:
        if (difference_from_lesser <= greater_square.root):
            return lesser_square.y + 1 - difference_from_lesser
        else:
            return greater_square.y


def calculate_distance_from_coordinates(x, y):
    return abs(x) + abs(y)


# easy part of just calling the method (:
calculate_num_steps(361527)
