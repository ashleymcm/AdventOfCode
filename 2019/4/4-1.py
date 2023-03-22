rangeStart = 206938
rangeEnd = 679128
possibleMatches = []

def doubleDigits(password):
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return True
    return False

def neverDecreases(password):
    for i in range(len(password) - 1):
        if int(password[i + 1]) < int(password[i]):
            return False
    return True

for password in range(rangeStart + 1, rangeEnd + 1):
    strPassword = str(password)
    if doubleDigits(strPassword) and neverDecreases(strPassword):
        possibleMatches.append(password)

print(len(possibleMatches))
