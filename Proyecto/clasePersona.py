from validador import *
from armado_menu import *
from claseInstitucion import *
from validadorLegajo import *
import os

clear = lambda : os.system('cls')

class Persona:
  def __init__(self, nombre_apellido, dni, sexo, fecha_nac):
    self.nombre_apellido = nombre_apellido
    self.dni = dni
    self.sexo = sexo
    self.fecha_nac = fecha_nac

class Alumno(Persona):

  def menu_registro_alumno(institucion:Institucion):
    x = "o"
    clear()

    legajo_ingresado = validadorLegajo(institucion)

    for alumno in institucion.alumnos:
        if alumno.legajo == legajo_ingresado:
          if alumno.sexo == "F":
            x = "a"
          return armado_menu(f"Bienvenid{x} {alumno.nombre_apellido}", ["Inscripcion a materias", "Iniciar Tramite", "Volver"], ['', ''])
          
  
    

  def __init__(self, nombre_apellido, dni, sexo, fecha_nac, legajo, materias_aprobadas, materias_en_curso, fecha_ingreso, carrera, estado_alumno, creditos_aprobados=0):
    super().__init__(nombre_apellido, dni, sexo, fecha_nac)
    self.legajo = legajo
    self.materias_aprobadas = []
    self.materias_en_curso = []
    self.fecha_ingreso = fecha_ingreso
    self.carrera = carrera
    self.estado_alumno = estado_alumno
    self.tramites_pendientes = []
    self.tramites_resueltos = []

 
  def __str__(self):
    return self.nombre_apellido
  
    

class Profesor(Persona):
  def menu_registro_profesor(institucion:Institucion):
    x = "o"
    legajo_ingresado = validadorLegajo(institucion)
    clear()
    for prof in institucion.profesores:
        if prof.legajo == legajo_ingresado:
          if prof.sexo == "F":
            x = "a"
          return armado_menu(f"Bienvenid{x} {prof.nombre_apellido}", ["Subir nota final", "Iniciar Tramite", "Volver"], ['', ''])


  def __init__(self, nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, fecha_baja=None, comisiones_acargo=None):
    super().__init__(nombre_apellido, dni, sexo, fecha_nac)
    self.legajo = legajo
    self.fecha_ingreso = fecha_ingreso
    self.fecha_baja = fecha_baja
    self.comisiones_acargo = []  

class Administrativo(Persona):
  def crear_administrativo(institucion:Institucion):
        nombre_apellido = input("Ingrese el nombre y apellido del administrativo: ")
        dni = input("Ingrese el DNI del empleado: ")
        fecha_nac = input("Ingrese la fecha de nacimiento: ")
        sexo = input("Ingrese el sexo: ")
        legajo = input("Ingrese el legajo: ")
        fecha_ingreso = input(f'Ingrese la fecha de ingreso a {institucion.nombre}: ')

        

        institucion.administrativos.append(Administrativo(nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso))
        print(f'El administrativo {nombre_apellido} se ha creado correctamente')
        print(len(institucion.administrativos))

  def menu_registro_administrativo(institucion:Institucion):
    x = "o"
    legajo_ingresado = validadorLegajo(institucion)
    clear()
    for admin in institucion.administrativos:
        if admin.legajo == legajo_ingresado:
          if admin.sexo == "F":
            x = "a"
          return armado_menu(f"Bienvenid{x} {admin.nombre_apellido}", ["Dar de alta alumno","Dar de baja alumno","Dar de alta profesor","Dar de baja profesor","Asignar titular de materia", "Tramites", "Volver"], ['', '', '','','',''])
  def __init__(self, nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, tramites_abiertos=[], tramites_resueltos=[], fecha_baja=None):
    super().__init__(nombre_apellido, dni, sexo, fecha_nac)
    self.legajo = legajo
    self.fecha_ingreso = fecha_ingreso
    self.fecha_baja = fecha_baja
    self.tramites_abiertos = tramites_abiertos
    self.tramites_resueltos = tramites_resueltos
    self.fecha_baja = fecha_baja
