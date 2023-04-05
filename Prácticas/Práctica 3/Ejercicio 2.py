def contar_caracter(string, caracter):
    contador = 0
    for i in string:
        if i == caracter:
            contador += 1
    
    return print(f'El caracter introducido: \'{caracter}\'\nCantidad de veces que se repitió: {contador}')

contar_caracter('Leo', 'o')