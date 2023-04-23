#from persona import *
from armado_menu import *
import os
from clasePersona import *
clear = lambda : os.system('cls')


def menu_principal():
    inicio = True
    while inicio:
        print("\n\t\tMENU PRINCIPAL\n\n1. Administrativo\n2. Alumno\n3. Profesor\n4. Salir")
        arranque = validador(4)
        clear()
        if arranque == 1:
            armado_menu("MENU ADMINISTRATIVO", ["Crear administrativo", "Iniciar sesion", "Salir"], [lambda : Administrativo.crear_administrativo(ITBA), lambda : Administrativo.menu_registro_administrativo(ITBA)])
        elif arranque == 2:
            armado_menu("MENU ALUMNO", ["Iniciar Sesion", "Salir"], [lambda : Alumno.menu_registro_alumno(ITBA)])
        elif arranque == 3:
            armado_menu("MENU PROFESOR", ["Iniciar Sesion", "Salir"], ["Hola Profesor Girafales"])
        elif arranque == 4:
            inicio = False
        
                
    
    print('Saliste del menu')

Leo = Alumno("Leonel Scalise",43046873,"M","fecha",62523,[],[],"fecha","negocios","vigente")
Juana = Alumno("Juana Santacreu",4112893,"F","fecha",234234,[],[],"fecha","negocios","vigente")
Mati = Alumno("Matías Díaz Cantón",43573875,"M","fecha",62473,[],[],"fecha","negocios","vigente")

ElAdmin = Administrativo("El Admin",4112893,"M","fecha",10000,"FECHA INGRESO",[],[])  # nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, tramites_abiertos, tramites_resueltos, fecha_baja=None
 

ITBA = Institucion("ITBA", "Pepe")

ITBA.agregar_alumno(Leo)
ITBA.agregar_alumno(Juana)
ITBA.agregar_alumno(Mati)

ITBA.agregar_administrativo(ElAdmin)


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


            

  