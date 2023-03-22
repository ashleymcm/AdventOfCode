from collections import Counter
import itertools


def check_valid_passwords():
    count = 0

    # take the spreadsheet from the file and split it in an array of "passwords"
    with open("input.txt") as password_list:
        passwords = [passwords.split() for passwords in password_list]

    # loop through all the passwords
    for password in passwords:
        valid = True
        # use itertools to compare each array element to every other array element
        for a, b in itertools.combinations(password, 2):
            # Counter will count the instances of each char in the strings
            if Counter(a) == Counter(b):
                # if they are the same then it's an anagram and we set valid to False
                valid = False
                break # we also break out of the loop to save time

        if valid:
            # add to the count if it's valid
            count = count + 1


    return count

check_valid_passwords()
