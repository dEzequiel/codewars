 def solution(string, markers):

    charIndex = 0
    #Todos los saltos de linea son reemplazados por un |, asi el string esta
    #solo en una unica linea, seguida, sin saltos de linea.
    string = string.replace('\n', '|')

    while charIndex < len(string):
        if string[charIndex] in markers:
            #Si no encuentras una barra, quita los espacios en blanco
            if string.find('|', charIndex) == -1:
                string = string[:charIndex].strip()
            else:
                string = string[:charIndex].strip() + string[string.find('|', charIndex):]
                charIndex = string.find('|', charIndex-1)
        charIndex += 1
    return string.replace('|', '\n')