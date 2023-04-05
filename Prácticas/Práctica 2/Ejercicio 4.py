# Realizar una función que dada una cadena que es una estructura de Datos no mutable, me permitamodificarla en una posición dada y un valor dado para esa posición

# def modif_string(string, posicion, valor):
#     list_string = list(string)
#     list_string[posicion] = valor
#     palabra = " ".join(list_string)
#     return palabra

# def modif_string(string, posicion, valor):
#     list_string = list(string)
#     list_string[posicion] = valor
#     palabra = "".join(list_string)

#     return print(palabra)


# modif_string("pelele", 3, "4")

# --------OTRA FORMA----------

def modif_string(string, posicion, valor):
    palabra = string[0:posicion] + valor + string[posicion + 1:]
    return print(palabra)

modif_string("pelele", 3, "4")