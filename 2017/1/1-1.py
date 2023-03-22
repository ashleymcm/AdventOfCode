def captcha_sum(captcha):
    # define sum and set it to nada
    sum = 0

    # take first character and add to end since it "wraps"
    captcha += captcha[0]

    # cycle through string checking for dupes
    index = 0
    while index < len(captcha) - 1:
        if captcha[index] == captcha[index + 1]:
            # add to sum if it's a dupe
            sum += int(captcha[index])
        index = index + 1

    return sum
