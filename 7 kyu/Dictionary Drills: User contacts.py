def user_contacts(data):

    for i in range(len(data)):
        if len(data[i]) == 1:
            data[i].append(None)

    D = dict(data)
    return D