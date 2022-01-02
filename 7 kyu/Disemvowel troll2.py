def disemvowel(string_):
    vowels = 'AEIOUaeiou'

    for char in vowels:
        string_ = string_.replace(char, "")

    return string_