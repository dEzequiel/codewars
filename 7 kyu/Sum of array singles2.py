def repeats(arr):

    sum = 0

    for occurrence in arr:
        if arr.count(occurrence) == 1:
            sum += occurrence

    return sum