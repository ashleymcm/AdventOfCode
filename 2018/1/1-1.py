import os, sys


dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

##loop through input rows, or "frequencies"
with open(os.path.join(dirname, "input.txt")) as frequency_list:
    frequencies = [frequencies.split() for frequencies in frequency_list]

current_frequency = 0

for frequency in frequencies:

    ##separate frequency into magnitude and direction
    direction = frequency[0][0]
    magnitude = int(frequency[0][1:])

    ##based on direction, add or subtract magnitude from current_frequency 
    if (direction == '+'):
        current_frequency += magnitude
    else:
        current_frequency -= magnitude


##print resulting frequency
print(current_frequency)
    