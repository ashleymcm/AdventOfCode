def increase_position(current_position, skip_size, length, arr):
    if (current_position + skip_size + length) > len(arr):
        current_position = (current_position + skip_size + length) % len(arr)
    else:
        current_position = current_position + skip_size + length
    return current_position


def ho_ho_hashed_array(current_position, skip_size, arr, lengths):

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

    return current_position, skip_size, arr


def densify(arr):
    xor = arr[0]
    for i in range(1, len(arr)):
        xor = xor ^ arr[i]

    return xor
    # return arr[0] ^ arr[1] ^ arr[2] ^ arr[3] ^ arr[4] ^ arr[5] ^ arr[6] ^ arr[7] ^ arr[8] ^ arr[9] ^ arr[10] ^ arr[11] ^ arr[12] ^ arr[13] ^ arr[14] ^ arr[15]


current_position = 0
skip_size = 0
arr = []
lengths = []
lengths_end_sequence = [17, 31, 73, 47, 23]
with open("input.txt") as fileObj:
    line = fileObj.readline().strip()
    for ch in line:
        lengths.append(ord(ch))
lengths = lengths + lengths_end_sequence

for i in range(256):
    arr.append(i)

for i in range(64):
    current_position, skip_size, arr = ho_ho_hashed_array(current_position, skip_size, arr, lengths)

dense_hash = []
arr_index = 0

while arr_index < 255:
    dense_hash.append(densify(arr[arr_index:arr_index + 16]))
    arr_index += 16

hex_string = ""
for x in dense_hash:
    new_hex = hex(x).replace("0x", "")
    if len(new_hex) < 2:
        new_hex = "0" + new_hex
    hex_string += new_hex

print(hex_string)
