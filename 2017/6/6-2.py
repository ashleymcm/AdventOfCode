from collections import Counter
import os, sys, itertools

def iterations_before_twin():
    count = 0
    history_of_banks = []
    old_length = 0
    done = False

    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
    # take the list of banks and turn it into an int array
    with open(os.path.join(dirname, "input.txt")) as banks_list:
        banks = [int(bank) for bank in banks_list.read().split()]
    print(banks)
    history_of_banks.append(list(banks))

    while not done:
        print("Banks begin: ", banks, len(history_of_banks))
        largest_bank_value = max(banks)
        largest_bank_index = banks.index(largest_bank_value)

        banks[largest_bank_index] = 0
        blocks_to_distribute = largest_bank_value
        list_index = largest_bank_index

        while blocks_to_distribute > 0:
            if list_index + 1 < len(banks):
                list_index = list_index + 1
            else:
                list_index = 0

            banks[list_index] = banks[list_index] + 1
            blocks_to_distribute = blocks_to_distribute - 1

        print("Banks end: ", banks, len(history_of_banks))
        for historic_banks in history_of_banks:
            if historic_banks == banks:
                print("true", historic_banks, banks)
                return len(history_of_banks) - history_of_banks.index(historic_banks)

        history_of_banks.append(list(banks))



print(iterations_before_twin())
