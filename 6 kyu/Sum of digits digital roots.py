def digital_root(n):

    numDigits = [int(numIndex) for numIndex in str(n)]

    n = sum(numDigits)

    while n > 9:
        secondNumDigits = [int(i) for i in str(n)]
        n = sum(secondNumDigits)

    return n