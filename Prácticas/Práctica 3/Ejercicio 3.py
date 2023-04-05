import string

def contador_caracteres(cadena):
    letras = 0
    numeros = 0
    especiales = 0
    lista = []
    for i in cadena:
        if i in string.ascii_letters:
            letras += 1
        elif i in string.digits:
            numeros += 1
        else:
            especiales += 1
    
    lista.append(letras)
    lista.append(numeros)
    lista.append(especiales)

    return lista


def caracter_mayor(funcion, cadena):
    letras = funcion(cadena)[0]
    numeros = funcion(cadena)[1]
    especiales = funcion(cadena)[2]
    mayor = max(letras, numeros, especiales)

    def separador(cadena):
        letters = ''
        numbers = ''
        specials = ''
        lista = []

        for i in cadena:
            if i in string.ascii_letters:
                if i.islower():
                    letters += i.upper()
                else:
                    letters += i.lower()
            elif i in string.digits:
                numbers += i
            else:
                specials += i
        
        lista.append(letters)
        lista.append(numbers)
        lista.append(specials)

        return lista

    print(f'Cantidad de letras: {letras}\nCantidad de números: {numeros}\nCantidad de especiales: {especiales}')

    if letras == mayor:
        print(separador(cadena)[0])
    elif numeros == mayor:
        print(separador(cadena)[1])
    else:
        print(separador(cadena)[2])



caracter_mayor(contador_caracteres,'OLA MINA XD')