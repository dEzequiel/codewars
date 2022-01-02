def duplicate_encode(word):

    word = word.lower()
    formatedText = ''

    for charIndex in word:
        numChar = word.count(charIndex)
        if numChar > 1:
            formatedText += ')'
        else:
            formatedText += '('
    return formatedText