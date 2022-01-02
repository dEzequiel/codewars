def shortcut( s ):
    # ...
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in s:
        if x in vowels:
            s = s.replace(x, "")
    return s;