def DNA_strand(dna):

    result = ""

    for i in dna:
        if i == 'T':
            result += i.replace(i, 'A')
        elif i == 'A':
            result += i.replace(i, 'T')
        elif i == 'G':
            result += i.replace(i, 'C')
        elif i == 'C':
            result += i.replace(i, 'G')
        else:
            return dna

    return result