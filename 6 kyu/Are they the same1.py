def comp(lista1, lista2):

    print(lista1)
    print(lista2)

    resultado = []

    #Si algunos de los dos no es nada, devuelveme False
    if lista1 == None or lista2 == None:
        return False

    #Si las dos listas estan vacias, devuelve True
    if not lista1 and not lista2:
        return True

    else:
        for elemento in range(0,len(lista1)):
        #
        # de la lista 1 hay que elevar cada elemento a 2
        # pow(2, 2)
            operacion = pow(lista1[elemento], 2)
            resultado.append(operacion)

        resultado.sort()
        lista2.sort()

    if resultado == lista2:
        return True
    else:
        return False