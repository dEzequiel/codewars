def calculate(n1, n2, o):
    def base2(i):
        return int(i, base=2)

    if o == 'add':
        resultado = base2(n1) + base2(n2)
    elif o == 'subtract':
        resultado = base2(n1) - base2(n2)
    elif o == 'multiply':
        resultado = base2(n1) * base2(n2)

    return '{0:b}'.format(resultado)
