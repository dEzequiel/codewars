def define_suit(card):
    # Good luck
    diccionario = {'C':'clubs', 'D':'diamonds', 'H':'hearts', 'S':'spades'}

    if card[-1] == 'C':
        return diccionario.get('C')
    elif card[-1] == 'D':
        return diccionario.get('D')
    elif card[-1] == 'H':
        return diccionario.get('H')
    elif card[-1] == 'S':
        return diccionario.get('S')
    else:
        return;