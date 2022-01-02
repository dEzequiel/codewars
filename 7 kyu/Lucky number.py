def is_lucky(n):

    #convert n int into string to treat them separatelly.
    n = str(n)
    numbers = [];
    sum = 0;

    #add each string to a list
    for x in n:
        numbers.append(x)

    #convert again each string element in the list into a int
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])

    #sum list elements between them
    for a in range(0, len(numbers)):
        sum += numbers[a]

    if sum % 9 == 0 or sum == 0:
        return True;
    else:
        return False;