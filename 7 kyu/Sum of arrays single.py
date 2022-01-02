def repeats(arr):

    sum = 0

    for occurence in arr:
        if arr.count(occurence) == 1:
            sum += occurence

    return sum