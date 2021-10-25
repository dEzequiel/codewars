def anagrams(word, words):
    
    result = [wordIndex for wordIndex in words if sorted(wordIndex) == sorted(word)]
    return result

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])