# simple dict that includes all values we're searching for
valid_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
}

# helper function to extract digits from a line. there are better ways, and even this could
# be optimized to minimize loops but i am a lazy girl and this is just for fun
def find_digits(line):
    # a place to store our digits, nice
    digits = []
    # loop through the indices of characters in the line
    for i in range(0, len(line)):
        # loop AGAIN (i never said this was performant) this time checking to see if the
        # substring starting at index i matches any of the digits we're looking for
        for digit, number in valid_digits.items():
            if (line.startswith(digit, i)):
                # if it's a match we append to our array and continue to the next iteration
                digits.append(number)
                continue
    
    return digits

# take the calibration document and split it in an array of lines
with open("input.txt") as calibration_document:
    lines = calibration_document.read().split("\n")

# create array to store the values once they're calculated
values = []

# loop through the lines
for line in lines:
    # use our nice lil helper function to get the digits
    digits = find_digits(line)
    # if there are two or more digits, combine the first and last and append to array
    if (len(digits) > 1):
        values.append(int(digits[0] + digits[-1]))
    # otherwise use just the first digit twice as the new number
    elif (len(digits) == 1):
        values.append(int(digits[0] + digits[0]))

# get the sum of the values
values_sum = sum(values)

# print it
print(values_sum)
