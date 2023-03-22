# this is the method that calculates the checksum and that should be called to solve the problem
def calculate_checksum():

    checksum = 0
    index = 0

    # take the spreadsheet from the file and split it in an array of "rows"
    with open("input.txt") as spreadsheet:
        rows = [rows.split() for rows in spreadsheet]

    # loop through all the rows
    while index < len(rows):
        # turn the whole string array into an int array to make the calcs below easier
        row = [int(cell) for cell in rows[index]]

        # sort list to make other calcs easier
        row.sort()

        # add quotient to checksum, calculated with method find_even_quotient() below
        checksum += find_even_quotient(row)

        index = index + 1

    return checksum


# this method loops through a row to calculate the quotient that divides easily to be added to checksum in calculate_checksum()
def find_even_quotient(row):

    index_divisor = 0                                         # an index for the divisor, starts from left so set to 0 every time

    # loop through all the smaller numbers - aka the left half of the array
    while index_divisor < len(row)/2:
        divisor = row[index_divisor]                          # get the value of the divisor
        index_dividend = len(row) - 1                         # an index of the dividend, starts from right so set to last item in array

        # loop through all the larger numbers - aka the right half of the array
        while index_dividend > len(row)/2 - 1:
            dividend = row[index_dividend]                    # get the value of the dividend

            # if modulo is 0 (aka false) we have a winner! return the quotient so it can be added to the checksum
            if not dividend % divisor:
                return dividend / divisor

            index_dividend = index_dividend - 1

        index_divisor = index_divisor + 1

    # we should never get this far without a return, if we do it means a row doesn't have an even quotient and that would just be mean
    return 0             
