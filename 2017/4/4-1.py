def check_valid_passwords():
    count = 0

    # take the spreadsheet from the file and split it in an array of "passwords"
    with open("input.txt") as password_list:
        passwords = [passwords.split() for passwords in password_list]

    # loop through all the passwords
    for password in passwords:
        # sets are collections of unique elements so if we turn the array
        # into a set and the length is different than the original we know
        # that there was a duplicate in there
        if len(password) == len(set(password)):
            count = count + 1

    return count

check_valid_passwords()
