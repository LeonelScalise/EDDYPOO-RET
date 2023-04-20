from validador import *
import os
clear = lambda : os.system('cls')

def armado_menu(nombre_menu, lista_opciones, lista_funciones):
    inicio_while = True
    while inicio_while:
        cont_opciones = 0
        print(f'\n\t\t{nombre_menu}\n')
        for texto in lista_opciones:
            cont_opciones += 1
            print(f'{cont_opciones}. {texto}')
        opcion_elegida = validador(cont_opciones)
        clear()
        if opcion_elegida == cont_opciones:
            inicio_while = False
        elif opcion_elegida == 1:
            print(lista_funciones[0])
        elif opcion_elegida == 2:
            print(lista_funciones[1])