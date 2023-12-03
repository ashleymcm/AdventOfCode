# take the calibration document and split it in an array of lines
with open("input.txt") as calibration_document:
    lines = calibration_document.read().split("\n")

# create array to store the values once they're calculated
values = []

# loop through the lines
for line in lines:
    # for each line we pull out the digits
    digits = [str(character) for character in line if character.isdigit()]
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
