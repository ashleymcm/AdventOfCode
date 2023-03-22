def calculate_checksum():

    checksum = 0
    index = 0

    # take the spreadsheet from the file and split it in an array of "rows"
    with open("input.txt") as spreadsheet:
        rows = [rows.split() for rows in spreadsheet]

    # loop through all the rows
    while index < len(rows):
        # turn the whole string array into an int array to make the calcs below easier
        int_row = [int(cell) for cell in rows[index]]

        # get difference
        difference = max(int_row) - min(int_row)

        # add difference to checksum
        checksum += difference

        index = index + 1

    return checksum
