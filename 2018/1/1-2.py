import os, sys


dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

##loop through input rows, or "frequencies"
with open(os.path.join(dirname, "input.txt")) as frequency_list:
    frequencies = [frequencies.split() for frequencies in frequency_list]

i = 0
current_frequency = 0
past_frequencies = []
duplicate_found = False

while not duplicate_found:

    frequency = frequencies[i]

    ##separate frequency into magnitude and direction
    direction = frequency[0][0]
    magnitude = int(frequency[0][1:])

    ##based on direction, add or subtract magnitude from current_frequency 
    if (direction == '+'):
        current_frequency += magnitude
    else:
        current_frequency -= magnitude

    ##if current_frquency has been seen before, break
    if (current_frequency in past_frequencies):
        duplicate_found = True
        break
    #else append this to past_frquencies and keep looking
    else:
        past_frequencies.append(current_frequency)

    ##control iteration through frequencies so that we can loop multiple times
    if (i < len(frequencies) - 1):
        i += 1
    else:
        i = 0

##print resulting frequency
print(current_frequency)