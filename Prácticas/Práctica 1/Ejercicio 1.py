# Ejercicio 1
import random

e = 0
Datos = []

while e <= 0:
    print("Codigo de registro Automotor")

    def menu_inicial():
        print("1. Registro \n2. Examen \n3. Verifiacion \n4. Salir")

    def menu():
        print("A. DNI \nB. Numero de tramite")

    menu_inicial()
    opcion_menu_inicial = int(input("Ingrese la opcion que desee:\n"))

    def Registro():
        datos_persona = []
        DNI = input("Ingrese numero de documento:\n")
        datos_persona.append(DNI)
        cod_empleado = input("Ingrese su codigo:\n")
        datos_persona.append(cod_empleado)
        tipo_lic = input("Ingrese Tipo de licencia:\n")
        datos_persona.append(tipo_lic)
        num_tramite = DNI + cod_empleado + tipo_lic
        datos_persona.append(num_tramite)

        if len(Datos) == 0:
            Datos.append(datos_persona)
        else:
            for i in range(0, len(Datos)):
                if DNI != Datos[i][0]:
                    Datos.append(datos_persona)
                else:
                    print("El DNI ya esta registrado")

    def Examen():
        menu()
        opcion_menu = input("Seleccione como validar su identidad:\n")

        if opcion_menu == 'A':
            verif_dni = input("Ingrese DNI:\n")
        elif opcion_menu == 'B':
            verif_tram = input("Ingrese numero de tramite:\n")
        else:
            print("Error: Ingrese A o B para continuar")

        if len(Datos) == 0:
            print("No hay usuarios registrados\n")
        else:
            for i in range(0, len(Datos)):
                if (verif_dni or verif_tram) in Datos[i]:
                    print("Rindio el examen")
                    nota_practico = random.randint(10, 100)
                    nota_teorico = random.randint(10, 100)
                    print(nota_practico, " y ", nota_teorico, "\n")
                    Datos[i].append(nota_practico)
                    Datos[i].append(nota_teorico)
                else:
                    print("El usuario no está registrado\n")

    def Verificacion():
        menu()
        opcion_menu = input("Seleccione como validar su identidad:\n")

        if opcion_menu == 'A':
            verif_dni = input("Ingrese DNI:\n")
        elif opcion_menu == 'B':
            verif_tram = input("Ingrese numero de tramite:\n")
        else:
            print("Ingrese A o B para continuar\n")

        if len(Datos) == 0:
            print("No hay usuarios registrados\n")
        else:
            for i in range(0, len(Datos)):
                if (verif_dni or verif_tram) in Datos[i]:
                    promedio = (Datos[i][4] + Datos[i][5]) / 2
                    if promedio >= 70:
                        print("Obtuvo el registro\n")
                    else:
                        print("No obtuvo el registro\n")

    if opcion_menu_inicial == 1:
        Registro()
    elif opcion_menu_inicial == 2:
        Examen()
    elif opcion_menu_inicial == 3:
        Verificacion()
    elif opcion_menu_inicial == 4:
        e += 1
        print("Registro de personas: ", Datos, "\n")
    else:
        print("Opcion invalida\n")
