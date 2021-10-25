def to_camel_case(text):

    if not text:
        return ''

    textWithoutSpecials = text

    for specialChar in textWithoutSpecials:
        if (specialChar == '-'):
            textWithoutSpecials = textWithoutSpecials.replace(specialChar, ' ')
        elif (specialChar == '_'):
            textWithoutSpecials = textWithoutSpecials.replace(specialChar, ' ')
        
    
    checkIfLower = textWithoutSpecials[0].islower()

    if checkIfLower:
        firstLetter = textWithoutSpecials[0].lower()
        capitalizedWords = textWithoutSpecials.title()
        formatedString = firstLetter + capitalizedWords.replace(capitalizedWords[0], '')
    else:
        formatedString = textWithoutSpecials.title()
        
    finalString = ''.join(formatedString.split())

    print(finalString)
    return finalString

if __name__ == '__main__':
    to_camel_case("Soy-el_amo")