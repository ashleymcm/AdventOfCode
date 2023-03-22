def increase_position(current_position, skip_size, length, arr):
    if (current_position + skip_size + length) > len(arr):
        current_position = (current_position + skip_size + length) % len(arr)
    else:
        current_position = current_position + skip_size + length
    return current_position

def ho_ho_hashed_array():
    current_position = 0
    skip_size = 0
    arr = []
    for i in range(256):
        arr.append(i)

    with open("input.txt") as lengths_list:
        lengths = [int(length) for length in lengths_list.read().split(",")]

    for length in lengths:

        if length > 2:
            if current_position + length > len(arr):
                start = current_position
                finish = length - len(arr) + start
                sub_arr = arr[start:len(arr)] + arr[0:finish]
                reversed_sub_arr = list(reversed(sub_arr))
                arr[start:len(arr)] = reversed_sub_arr[0:(len(arr)-start)]
                arr[0:finish] = reversed_sub_arr[len(arr)-start:]

            else:
                start = current_position
                finish = start + length
                sub_arr = arr[start:finish]
                arr[start:finish] = list(reversed(sub_arr))

        current_position = increase_position(current_position, skip_size, length, arr)

        skip_size += 1

    return(arr[0] * arr[1])


print(ho_ho_hashed_array())
