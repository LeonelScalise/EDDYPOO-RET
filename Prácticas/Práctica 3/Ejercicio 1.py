import string

def contador_caracteres(cadena):
    letras = 0
    numeros = 0
    especiales = 0
    for i in cadena:
        if i in string.ascii_letters:
            letras +=1
        elif i in string.digits:
            numeros += 1
        else:
            especiales += 1
    
    return print(f'Cantidad de letras: {letras}\nCantidad de números: {numeros}\nCantidad de especiales: {especiales}')
    

contador_caracteres('Yo se que algunas veces me equivoco demasiado')
