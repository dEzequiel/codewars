def narcissistic(value):

    string = str(value);
    list = [];
    list_operation = [];
    sum = 0;

    print(string)

    for x in string:
        number = int(x)
        list.append(number)

    list_len = len(list);

    for i in range(0, len(list)):
        operation = list[i] ** list_len
        list_operation.append(operation)

    print(list)
    print(list_operation)

    for z in list_operation:
        sum += z

    if value == sum:
        return True;
    else:
        return False;