import os, sys

# i hate that i need this when i'm on my windows machine
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

# loop through input rows, or "binaries"
with open(os.path.join(dirname, "input.txt")) as binaries_list:
  binaries = [binaries.rstrip() for binaries in binaries_list]

def checkPowerConsumption(binaries):

  one_counter = [0] * len(binaries[0])
  half_length = len(binaries)/2

  # loop through binaries and count the occurrence that we see a 1 in each index
  for binary in binaries:
    for i in range(0, len(binary)):
      if binary[i] == '1':
        one_counter[i] += 1

  # create lists to help calculate our rates
  gamma_rate = list()
  epsilon_rate = list()

  # loop through the counter we created above and if the count is greater than half
  # the length of the number of binaries then we know it is the most commonly occurred,
  # otherwise 0 is the most commonly occurred - we append to our rates based on this in
  # the instructions
  for one_count in one_counter:
    if one_count > half_length:
      gamma_rate.append('1')
      epsilon_rate.append('0')
    else:
      gamma_rate.append('0')
      epsilon_rate.append('1')

  # now our rates are binaries represented as lists of strings of 1s and 0s, but we need 
  # to turn the back into decimal numbers so that we can multiply them and get our answer
  gamma_rate = int("".join(gamma_rate), 2)
  epsilon_rate = int("".join(epsilon_rate), 2)

  return gamma_rate * epsilon_rate

print(checkPowerConsumption(binaries))