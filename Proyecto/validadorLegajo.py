from claseInstitucion import *
import os

clear = lambda : os.system('cls')

def validadorLegajo(institucion):
    inicio = True

    while inicio: #arranca el loop
        try: #intenta pedir una respuesta
            legajoingresado = int(input("Ingrese su numero de legajo: "))
            clear()
            if legajoingresado not in institucion.legajos:
                raise Exception("\nEl legajo no existe, intente nuevamente.\n") #si no cumple con la condición que se indica levanta un error con un mensaje
            else:
                inicio = False #frena el loop si está todo ok
        except ValueError: #si ingresan un tipo de dato incorrecto no se rompe el sistema sino que te vuelve a pedir una rta.
            print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e: 
            print(e) #imprime el mensaje que vos indicaste antes
    
    return legajoingresado