#from persona import *
from armado_menu import *
import os
clear = lambda : os.system('cls')


def menu_principal():
    inicio = True
    while inicio:
        arranque = int(input("\n\t\tMENU PRINCIPAL\n\n1. Administrativo\n2. Alumno\n3. Profesor\n4. Salir\n\nSeleccione una opcion: "))
        clear()
        if arranque == 1:
            armado_menu("MENU ADMINISTRATIVO",["Crear administrativo", "Iniciar sesion", "Salir"], ["Hola 1", "Hola 2"])
        elif arranque == 2:
            armado_menu("MENU ALUMNO",["Iniciar Sesion", "Salir"], ["Hola Alumno"])
        elif arranque == 3:
            armado_menu("MENU PROFESOR",["Iniciar Sesion", "Salir"], ["Hola Profesor Girafales"])
        elif arranque == 4:
            inicio = False
        
                
                
                
    
    print('Saliste del menu')

menu_principal()












# OTRA FORMA DE HACER EL MENU
# def menu_principal():
#     inicio = True
#     while inicio:
#         arranque = int(input("Seleccione una opcion:\n1. Administrativo\n2. Alumno\n3. Profesor\n4. Salir\n"))
#         clear()
#         if arranque == 1:
#             inicio_admin = True
#             while inicio_admin:
#                 print('Elija opcion:\n1. Crear administrativo\n2. Iniciar sesión\n3. Salir\n')
#                 opcion_administrativo = validador(3)
#                 clear()
#                 if opcion_administrativo == 1:
#                     print("aca iria el menu administrativo para crear")
#                 elif opcion_administrativo == 2:
#                     print("aca iria el menu para ingresar como administrativo")
#                 elif opcion_administrativo == 3:
#                     inicio_admin = False
#         elif arranque == 2:
#             inicio_alumno = True
#             while inicio_alumno:
#                 print('Elija opcion:\n1. Iniciar sesión\n2. Salir\n')
#                 opcion_alumno = validador(2)
#                 clear()
#                 if opcion_alumno == 1:
#                     print("aca iria menu de inicio de sesion de alumno")
#                 elif opcion_alumno == 2:
#                     inicio_alumno = False
#         elif arranque == 3:
#             inicio_prof = True
#             while inicio_prof:
#                 print('Elija opcion:\n1. Iniciar sesión\n2. Salir\n')
#                 opcion_prof = validador(2)
#                 clear()
#                 if opcion_prof == 1:
#                     print("aca iria menu de inicio de sesion de prof")
#                 elif opcion_prof == 2:
#                     inicio_prof = False
#         elif arranque == 4:
#             inicio = False
                
                
                
    
#     print('Termino el codigo')


            

  