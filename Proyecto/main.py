from clases import *

def menu_interactivo(institucion_educativa):
    while True:
        print("Opciones:")
        print("1. Ver materias disponibles")
        print("2. Inscribirse a una materia")
        print("3. Ver mis materias inscriptas")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            # Mostrar lista de materias disponibles
            print("Materias disponibles:")
            for materia in institucion_educativa.materias_disponibles:
                print(materia)
        elif opcion == "2":
            # Pedir datos al usuario y agregar materia al estudiante
            print("Ingrese sus datos:")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            numero_legajo = input("Número de legajo: ")
            carrera = input("Carrera: ")
            sede = input("Sede: ")
            materia_nombre = input("Nombre de la materia: ")
            comision_numero = input("Número de comisión: ")

            # Crear estudiante
            estudiante = Estudiante(nombre, apellido, dni, numero_legajo, carrera, True, sede)

            # Buscar materia y comisión
            materia = institucion_educativa.buscar_materia(materia_nombre)
            if materia is None:
                print("Materia no encontrada")
                continue
            comision = materia.buscar_comision(comision_numero)
            if comision is None:
                print("Comisión no encontrada")
                continue

            # Agregar materia al estudiante
            exito = estudiante.agregar_materia(materia, comision)
            if exito:
                print("Inscripción exitosa")
            else:
                print("No se pudo inscribir a la materia")
        elif opcion == "3":
            # Mostrar lista de materias inscriptas por el estudiante
            print("Mis materias:")
            for materia in institucion_educativa.materias:
                for comision in materia.comisiones:
                    if estudiante in comision.alumnos:
                        print(f"{materia.nombre} - {comision.numero}")
        elif opcion == "4":
            # Salir del programa
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")


#institucion_educativa = InstitucionEducativa()
#menu_interactivo(institucion_educativa)