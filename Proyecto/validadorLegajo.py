from claseInstitucion import *
import os
from armado_menu import *

clear = lambda : os.system('cls')


def reintento():
    print("1. Reintentar\n2. Volver")
    eleccion = validador(2)
    if eleccion == 1:
        clear()
        return True
    elif eleccion == 2:
        clear()
        return False
        
    

def validadorLegajo(institucion):
    inicio = True

    while inicio: #arranca el loop
        try: #intenta pedir una respuesta
            legajoingresado = int(input("Ingrese su numero de legajo: "))
            clear()
            if len(str(legajoingresado)) != 5:
                raise Exception("\nEl legajo debe ser un numero de 5 digitos.\n") 
            if legajoingresado not in institucion.legajos:
                raise Exception("\nEl legajo no existe, intente nuevamente.\n") #si no cumple con la condición que se indica levanta un error con un mensaje
            else:
                inicio = False #frena el loop si está todo ok
        except ValueError: #si ingresan un tipo de dato incorrecto no se rompe el sistema sino que te vuelve a pedir una rta.
            print('\nEl dato introducido no corresponde al valor esperado.\n')
            inicio = reintento()
        except Exception as e: 
            print(e)      #imprime el mensaje que vos indicaste antes
            inicio = reintento() 
    return legajoingresado