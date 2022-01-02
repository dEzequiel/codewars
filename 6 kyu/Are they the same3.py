def comp(array1, array2):

    list_results = [];
    print(array1)
    print(array2)

    if array1 == None or array2 == None:
        return False;
    else:
        for i in range(0, len(array1)):
            x = pow(array1[i], 2)
            list_results.append(x)

    if sorted(list_results) == sorted(array2):
        return True;
    else:
        return False;