def anagrams(word, words):
    
    result = []

    #wordsIndex es la  referencia de cada palabra dentro del la lista words.
    for wordsIndex in words:
        '''Si ordenas la word mediante sorted te da los caracteres ordenados de cierta forma. Pues si ordenas los demas
        elementos de la lista words, y estos coinciden con la posicion de los elementos con la de word organizada pues
        es un anagrama. Es true'''
        if sorted(word) == sorted(wordsIndex):              
            result.append(wordsIndex)
        else:
            continue
    
    return result