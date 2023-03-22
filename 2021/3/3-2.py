import os, sys

# i hate that i need this when i'm on my windows machine
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

# loop through input rows, or "binaries"
with open(os.path.join(dirname, "input.txt")) as binaries_list:
  binaries = [binaries.rstrip() for binaries in binaries_list]

# helper method that gets bit criteria according to oxygen generator rating,
# the co2 one is actually just the inverse of this one so we create another helper
# below to invert it
def getBitCriteria(binary_list, index):
  
  half_length = len(binary_list)/2
  one_counter = 0
  
  for binary in binary_list:
    if binary[index] == '1':
      one_counter += 1

  if one_counter >= half_length:
    return '1'
  
  return '0'

def invertBitCriteria(bit_criteria):
  
  if bit_criteria == '1':
      return '0'
  
  return '1'

# small helper that determines if a bit matches the bit criteria for use in the
# list comprehensions below
def matchesBitCriteria(binary, index, bit_criteria):
  
  return binary[index] == bit_criteria

# we loop through all the values until we have only one remaining, according to 
# the bit criteria and what matches it, then return that remaining value
def getOxygenGeneratorRating(original_list):

  oxygen_list = original_list.copy()
  index = 0

  while len(oxygen_list) != 1:
    bit_criteria = getBitCriteria(oxygen_list, index)
    oxygen_list[:] = [x for x in oxygen_list if matchesBitCriteria(x, index, bit_criteria)]
    index += 1

  return oxygen_list[0]

# this method is nearly identical to the one above, with the only difference that we 
# invert the bit criteria. there's definitely room for refactoring but i'm lazy and i 
# also like how nice and readable the main method below is right now :) 
def getCo2ScrubberRating(original_list):
  
  co2_list = original_list.copy()
  index = 0

  while len(co2_list) != 1:
    bit_criteria = getBitCriteria(co2_list, index)
    bit_criteria = invertBitCriteria(bit_criteria)

    co2_list[:] = [x for x in co2_list if matchesBitCriteria(x, index, bit_criteria)]
    index += 1

  return co2_list[0]

# to get the life support rating we just get the oxygen generator and co2 scrubbing ratings,
# turn them into integers, and multiply them to return the product
def getLifeSupportRating(binaries):

  oxygen_rating = getOxygenGeneratorRating(binaries)
  co2_rating = getCo2ScrubberRating(binaries)

  oxygen_rating = int(oxygen_rating, 2)
  co2_rating = int(co2_rating, 2)

  return oxygen_rating * co2_rating

print(getLifeSupportRating(binaries))