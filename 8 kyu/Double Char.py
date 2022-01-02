def double_char(s):

    characters = list(s)
    charactersMultiplyed = []

    for char in characters:
        char = char * 2
        charactersMultiplyed.append(char)

    finalString = ''.join(charactersMultiplyed)

    return finalString