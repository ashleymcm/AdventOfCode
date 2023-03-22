A = 289
B = 629
Amul = 16807
Bmul = 48271
divisor = 2147483647
match = 0

for i in range(5000000):
    listA = list(bin(A))
    listB = list(bin(B))
    if listA[-16:] == listB[-16:]:
        match += 1
    A = (A * Amul) % divisor
    while A % 4 != 0:
        A = (A * Amul) % divisor
    B = (B * Bmul) % divisor
    while B % 8 != 0:
        B = (B * Bmul) % divisor

print(match)
