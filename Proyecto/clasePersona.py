from validador import *
from armado_menu import *
from claseInstitucion import *
import os

clear = lambda : os.system('cls')



class Persona:
  def __init__(self, nombre_apellido, dni, sexo, fecha_nac):
    self.nombre_apellido = nombre_apellido
    self.dni = dni
    self.sexo = sexo
    self.fecha_nac = fecha_nac

class Alumno(Persona):
  legajo_alumnos = []

  def menu_registro_alumno(institucion:Institucion):
    
    legajo_ingresado = int(input("Ingrese su numero de legajo: "))
    clear()
    for alumno in institucion.alumnos:
        if alumno.legajo == legajo_ingresado:
          return print(f"Bienvenido {alumno.nombre_apellido}")


  def __init__(self, nombre_apellido, dni, sexo, fecha_nac, legajo, materias_aprobadas, materias_en_curso, fecha_ingreso, carrera, estado_alumno, creditos_aprobados=0):
    super().__init__(nombre_apellido, dni, sexo, fecha_nac)
    self.legajo = int(legajo)
    self.materias_aprobadas = []
    self.materias_en_curso = []
    self.fecha_ingreso = fecha_ingreso
    self.carrera = carrera
    self.estado_alumno = estado_alumno
    self.tramites_pendientes = []
    self.tramites_resueltos = []

  #def menu_alumno(self):
   # print(f"\t\t\nBienvenido {self.nombre_apellido}\n")
    
#  def menu_registro_alumno(self, institucion):
#   legajo_ingresado = int(input("Ingrese su numero de legajo: "))

  
  def __str__(self):
    return self.nombre_apellido
  
    

class Profesor(Persona):
  def __init__(self, nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, fecha_baja=None, comisiones_acargo=None):
    super().__init__(nombre_apellido, dni, sexo, fecha_nac)
    self.legajo = legajo
    self.fecha_ingreso = fecha_ingreso
    self.fecha_baja = fecha_baja
    self.comisiones_acargo = []  

class Administrativo(Persona):
  def menu_registro_administrativo(institucion:Institucion):
    
    legajo_ingresado = int(input("Ingrese su numero de legajo: "))
    clear()
    for admin in institucion.administrativos:
        if admin.legajo == legajo_ingresado:
          print(f"Bienvenido {admin.nombre_apellido}")

  def __init__(self, nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, tramites_abiertos, tramites_resueltos, fecha_baja=None):
    super().__init__(nombre_apellido, dni, sexo, fecha_nac)
    self.legajo = legajo
    self.fecha_ingreso = fecha_ingreso
    self.fecha_baja = fecha_baja
    self.tramites_abiertos = []
    self.tramites_resueltos = []
