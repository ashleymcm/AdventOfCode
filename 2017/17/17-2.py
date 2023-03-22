array = []
step = 369

for i in range(50000001):
    index = step
    if i == 0:
        array.append(0)
        continue

    if step >= i:
        index = step % i

    index += 1
    array.insert(index, i)
    array = array[index:] + array[0:index]

print(array[array.index(0) + 1])
