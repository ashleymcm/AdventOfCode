def captcha_sum(captcha):
    # define sum and set it to nada
    sum = 0
    #define length and half_length - not necessary but makes it look a bit nicer
    length = len(captcha)
    half_length = len(captcha)//2

    # add half the string again to the end since it "wraps"
    captcha += captcha[0:half_length]

    # cycle through string checking for dupes
    index = 0
    while index < length:
        if captcha[index] == captcha[index + half_length]:
            # add to sum if it's a dupe
            sum += int(captcha[index])
        index = index + 1

    return sum
