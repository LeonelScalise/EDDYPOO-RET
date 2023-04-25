from validador import *
from armado_menu import *
from claseInstitucion import *
from validadorLegajo import *
import os
from claseTramite import *
import random
from popularInstitucion import ITBA

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
    legajo_ingresado = validadorLegajo(institucion)
    clear()
    for alumno in institucion.alumnos:
        if alumno.legajo == legajo_ingresado:
          if alumno.sexo == "F":
            x = "a"
          return armado_menu(f"Bienvenid{x} {alumno.nombre_apellido}", ["Inscripcion a materias", "Iniciar Tramite", "Volver"], ["", lambda : alumno.iniciarTramite(ITBA)])
          
  
    

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
  

  def iniciarTramite(self,institucion):
    id_tramite = 0

    if len(institucion.historial_tramites)!= 0:
      id_tramite= institucion.historial_tramites[-1].id+1
    tipo_de_tramite = input("Ingrese el tipo de tramite: ")
    cantidad_administrativos = len(institucion.administrativos)
    i_random = random.randint(0,cantidad_administrativos-1)
    administrativo_asignado=institucion.administrativos[i_random]
    nuevo_tramite = Tramite(id_tramite,self,administrativo_asignado,tipo_de_tramite,"24/4/2023")
    administrativo_asignado.tramites_abiertos.append(nuevo_tramite)
    institucion.tramites_abiertos.append(nuevo_tramite)
    institucion.historial_tramites.append(nuevo_tramite) 
    return print("Ya iniciaste el tramite")

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
          return armado_menu(f"Bienvenid{x} {admin.nombre_apellido}", ["Dar de alta alumno","Dar de baja alumno","Dar de alta profesor","Dar de baja profesor","Asignar titular de materia", "Tramites", "Volver"], ['', '', '','','',lambda : admin.displayTramiteActivo()])
        
  def __init__(self, nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, fecha_baja=None):
    super().__init__(nombre_apellido, dni, sexo, fecha_nac)
    self.legajo = legajo
    self.fecha_ingreso = fecha_ingreso
    self.fecha_baja = fecha_baja
    self.tramites_abiertos = []
    self.tramites_resueltos = []
    self.fecha_baja = fecha_baja
  
  def __str__(self):
      return "{} es administrativo y tiene el legajo {}".format(self.nombre_apellido,self.legajo)

  def  tramitesActivos(self):
    lista_tramites = ["SALIR - NO HAY TRAMITES POR RESOLVER"]
    if self.tramites_abiertos != []:
      lista_tramites = []
      for tramite in self.tramites_abiertos:
        lista_tramites.append(tramite.tipo_de_tramite)
      lista_tramites.append("Volver")
    return lista_tramites
  
  def funcionResolverTramite(self, texto_tramite):
    armado_menu(texto_tramite, ["Resolver tramite", "Volver"], [lambda : 2+2])

  def resolverTramite(self):
    lista_funciones = []
    
    def funcion_mascara(tramite):
        return lambda: self.funcionResolverTramite(f'¿Quiere resolver el tramite "{tramite.tipo_de_tramite}" del alumno {tramite.alumno.nombre_apellido}?')
    
    for tramite in self.tramites_abiertos:
        lista_funciones.append(funcion_mascara(tramite))
    
    return lista_funciones
    


  def displayTramiteActivo(self):
    lista_tramites = self.tramitesActivos()
    lista_funciones = self.resolverTramite()
    armado_menu('Tramites pendientes', lista_tramites, lista_funciones)

if __name__=="__main__":
  ITBA = Institucion("ITBA", "Pepe")

  Leo = Alumno("leonel",4344893,"M","fecha","Legajo de leo",[],[],"fecha","negocios","vigente")
  Fede = Alumno("fede",4112893,"M","fecha","Legajo de fede",[],[],"fecha","negocios","vigente")

  administrativo_1=Administrativo("Nombre administrativo 1",45678901,"m","01/01/2000",61230,"01/01/2020")
  # administrativo_2=Administrativo("Nombre administrativo 2",46678902,"m","01/01/2001",61231,"02/02/2020")
  # administrativo_3=Administrativo("Nombre administrativo 3",47678903,"m","01/01/2002",61233,"03/03/2020")

  ITBA.agregar_alumno(Leo)
  ITBA.agregar_alumno(Fede)
  ITBA.agregar_administrativo(administrativo_1)
  # ITBA.agregar_administrativo(administrativo_2)
  # ITBA.agregar_administrativo(administrativo_3)

  Leo.iniciarTramite(ITBA)
  Leo.iniciarTramite(ITBA)
  Leo.iniciarTramite(ITBA)

  print("-----------")
  print(len(administrativo_1.tramites_abiertos))
  # print(len(administrativo_2.tramites_abiertos))
  # print(len(administrativo_3.tramites_abiertos))