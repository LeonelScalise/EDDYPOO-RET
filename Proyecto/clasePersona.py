from logging import raiseExceptions
from validadorInputs import *
from armado_menu import *
from claseInstitucion import *
from validadorLegajo import *
import os
from claseTramite import *
import random
from popularInstitucion import ITBA
from claseCarrera import *

clear = lambda : os.system('cls')

class Persona:
  def __init__(self, nombre_apellido, dni, sexo, fecha_nac):
    # bandera=True
    # while bandera:
    #   try:
    #     self.dni=int(dni)
    #     if len(dni)<7:
    #       raise Exception ("\nEl DNI no tiene los caracteres suficientes.\n")
    #     else:
    #       bandera=False
    #   except ValueError: #si ingresan un tipo de dato incorrecto no se rompe el sistema sino que te vuelve a pedir una rta.
    #         print('\nEl dato introducido no corresponde al valor esperado.\n')
    #   except Exception as e: 
    #         print(e) #imprime el mensaje que vos indicaste antes
    while not dni.isdigit():
        print("El dni debe ser un entero")
        dni = input("Ingresar dni: ")
    self.dni=dni
    self.nombre_apellido = nombre_apellido
    self.sexo = sexo
    self.fecha_nac = fecha_nac

class Alumno(Persona):

  def menu_registro_alumno(institucion:Institucion):
    x = "o"
    legajo_ingresado = validadorLegajoAlumnos(institucion)
    clear()
    for alumno in institucion.alumnos:
        if alumno.legajo == legajo_ingresado:
          if alumno.sexo == "F":
            x = "a"
          return armado_menu(f"Bienvenid{x} {alumno.nombre_apellido}", ["Inscripcion a materias", "Iniciar Tramite", "Volver"], [lambda : alumno.inscribirMateria(), lambda : alumno.iniciarTramite(ITBA)])

    
#Borrar materias_aprobadas y materias_en_curso del INIT.

#Pongo que carrera por predeterminado este vacio, porque no le puedo poner un input
#de que ingrese la carrera del alumno, porque ahi tiene que haber un objeto carrera.
#Entonces tengo que poner predeterminado vacio, y darle al administrativo las opciones
#de carrera para que anote al alumno.
#El estado del alumno tiene que ser "Activo" por defecto.

  def __init__(self, nombre_apellido, dni, sexo, fecha_nac, legajo,fecha_ingreso,estado_alumno="Activo", carrera="", creditos_aprobados=0):
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

    if len(institucion.historial_tramites) != 0:
      id_tramite= institucion.historial_tramites[-1].id + 1
    tipo_de_tramite = input("Ingrese el tipo de tramite: ")
    cantidad_administrativos = len(institucion.administrativos)
    i_random = random.randint(0,cantidad_administrativos-1)
    administrativo_asignado=institucion.administrativos[i_random]
    nuevo_tramite = Tramite(id_tramite,self,administrativo_asignado,tipo_de_tramite,"24/4/2023")
    administrativo_asignado.tramites_abiertos.append(nuevo_tramite)
    institucion.tramites_abiertos.append(nuevo_tramite)
    institucion.historial_tramites.append(nuevo_tramite) 
    return print("Ya iniciaste el tramite")
  
  def inscribirMateria(self):
    materias_disponibles = []
    c = 0
    for materia in self.carrera.materias:
      if len(materia.correlativas) != 0:
        for corre in materia.correlativas:
          if corre in self.materias_aprobadas:
            c += 1
          if c == len(materia.correlativas) and materia not in self.materias_aprobadas and materia not in self.materias_en_curso:
            materias_disponibles.append(materia.nombre)   
      elif materia not in self.materias_aprobadas and materia not in self.materias_en_curso:
        materias_disponibles.append(materia.nombre)

    armado_menu(f"Materias disponibles para incripcion de {self.nombre_apellido}", materias_disponibles, [f"Se ha incripto a {materias_disponibles[0]} correctamente",f"Se ha incripto a {materias_disponibles[1]} correctamente"])

        

class Profesor(Persona):
  def menu_registro_profesor(institucion:Institucion):
    x = "o"
    legajo_ingresado = validadorLegajoProfe(institucion)
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
    legajo_ingresado = validadorLegajoAdmin(institucion)
    clear()
    for admin in institucion.administrativos:
        if admin.legajo == legajo_ingresado:
          if admin.sexo == "F":
            x = "a"
<<<<<<< HEAD
          return armado_menu(f"Bienvenid{x} {admin.nombre_apellido}", ["Dar de alta alumno","Dar de baja alumno","Dar de alta profesor","Dar de baja profesor","Asignar titular de materia", "Tramites", "Volver"], ['', '', '','','',''])
=======
          return armado_menu(f"Bienvenid{x} {admin.nombre_apellido}", ["Dar de alta alumno","Dar de baja alumno","Dar de alta profesor","Dar de baja profesor","Asignar titular de materia", "Tramites", "Volver"], [lambda : admin.altaAlumno(), '', lambda : admin.altaProfesor(),'','',lambda : admin.displayTramiteActivo()])
>>>>>>> f5c2483c238d8afc598041aac88e307d02f99351
        
  def __init__(self, nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, fecha_baja=None):
    super().__init__(nombre_apellido, dni, sexo, fecha_nac)
    self.legajo = legajo
    self.fecha_ingreso = fecha_ingreso
    self.fecha_baja = fecha_baja
    self.tramites_abiertos = []
    self.tramites_resueltos = []
    self.fecha_baja = fecha_baja

  
  def asignarProfesor(self):
    pass
    


  
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
  
  def tacharTramite(self, id_tram):
      for tramite in self.tramites_abiertos:
        if tramite.id == id_tram:
          #Si esta, tengo que eliminarlo de las listas que estan en Institución y la propia lista del administrativo
          ITBA.tramites_abiertos.remove(tramite)
          self.tramites_abiertos.remove(tramite)
        #Una vez que lo saco de las listas, tengo que cambiar el estado del tramite a "Resuelto"
          tramite.estado="Resuelto"
        #Una vez que le cambio el estado, tengo que poner el tramite en la lista de tramites resueltos de la Institución y el administrativo
          ITBA.tramites_resueltos.append(tramite)
          self.tramites_resueltos.append(tramite)
          return print("El tramite {} ha sido resuelto".format(tramite.tipo_de_tramite))
      clear()
    

  def resolverTramite(self, texto_tramite, id_tramite):
    armado_menu(texto_tramite, ["Resolver tramite", "Volver"], [lambda : self.tacharTramite(id_tramite)])

  
  
  def listaFuncTramite(self):
    lista_funciones = []
    
    def funcion_mascara(tramite):
        return lambda: self.resolverTramite(f'¿Quiere resolver el tramite "{tramite.tipo_de_tramite}" del alumno {tramite.alumno.nombre_apellido}?', tramite.id)
    
    for tramite in self.tramites_abiertos:
        lista_funciones.append(funcion_mascara(tramite))
    
    return lista_funciones
    
  def displayTramiteActivo(self):
    lista_tramites = self.tramitesActivos()
    lista_funciones = self.listaFuncTramite()
    armado_menu('Tramites pendientes', lista_tramites, lista_funciones)



  def altaAlumno(self):
    nombre = input("Ingrese el nombre del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")
    sexo = input("Ingrese el sexo del alumno: ")
    fecha_nacimiento= input("Ingrese la fecha de nacimiento del alumno: ")
    if len(ITBA.legajos_alumnos)!= 0:
      legajo = ITBA.legajos_alumnos[-1]+1
    else:
      legajo=10000
    fecha_ingreso = input("Ingrese la fecha de ingreso del alumno: ")
    contador=1
    opciones=[]

    alumno_nuevo=Alumno(nombre,dni,sexo,fecha_nacimiento,legajo,fecha_ingreso)
    clear()
    #Para que el administrativo anote al alumno en un objeto carrera
    print(f'\n\t\t Ingrese la carrera del alumno\n')
    for carrera in ITBA.carreras:
      print(("{}. {}").format(contador,carrera.nombre))
      opciones.append(contador)
      contador+= 1
    #Hay que validar la opción elegida
    opcion_elegida = int(input("Ingrese la opción: "))
    while opcion_elegida not in opciones:
      opcion_elegida = int(input("Opción no valida, intente nuevamente: "))
    alumno_nuevo.carrera = ITBA.carreras[opcion_elegida-1]
    clear()
    print("Se ha anotado al alumno a la carrera: ",alumno_nuevo.carrera.nombre)
    ITBA.agregar_alumno(alumno_nuevo)
    alumno_nuevo.carrera.alumnos_actuales.append(alumno_nuevo)

  def altaProfesor(self):
    nombre = input("Ingrese el nombre del profesor: ")
    dni = input("Ingrese el DNI del profesor: ")
    sexo = input("Ingrese el sexo del profesor: ")
    fecha_nacimiento= input("Ingrese la fecha de nacimiento del profesor: ")
    if len(ITBA.legajos_profesores)!= 0:
      legajo_numero = int(ITBA.legajos_profesores[-1][2:])+1
      legajo_alfa = "PR"
      legajo= legajo_alfa+str(legajo_numero)
    else:
      legajo="PR10000"
    fecha_ingreso = input("Ingrese la fecha de ingreso del profesor: ")

    profesor_nuevo=Profesor(nombre,dni,sexo,fecha_nacimiento,legajo,fecha_ingreso)
    ITBA.agregar_profesor(profesor_nuevo)



if __name__=="__main__":
  ITBA = Institucion("ITBA", "Pepe")

  Leo = Alumno("leonel",4344893,"M","fecha",23456,"fecha")
  Fede = Alumno("fede",4112893,"M","fecha",12345,"fecha")

  administrativo_1=Administrativo("Nombre administrativo 1",45678901,"m","01/01/2000",61230,"01/01/2020")
  # administrativo_2=Administrativo("Nombre administrativo 2",46678902,"m","01/01/2001",61231,"02/02/2020")
  # administrativo_3=Administrativo("Nombre administrativo 3",47678903,"m","01/01/2002",61233,"03/03/2020")
  ITBA.agregar_administrativo(administrativo_1)
  # ITBA.agregar_administrativo(administrativo_2)
  # ITBA.agregar_administrativo(administrativo_3)

  # Leo.iniciarTramite(ITBA)
  # Leo.iniciarTramite(ITBA)
  # Leo.iniciarTramite(ITBA)

  licnegocios=Carrera("Negocios",196,"Luis")
  licnanalitica=Carrera("Analitica",196,"Juan")
  inginformatica=Carrera("Ingenieria Informatica",250,"Mario")
  ingindustrial=Carrera("Ingenieria Industrial",250,"Andres")

  ITBA.agregar_carrera(licnegocios)
  ITBA.agregar_carrera(licnanalitica)
  ITBA.agregar_carrera(ingindustrial)
  ITBA.agregar_carrera(inginformatica)

  # administrativo_1.altaAlumno()
  profe=Profesor("Pepe",1232141,"M","01/01/2020","PR10000","02/01/2020")
  ITBA.agregar_profesor(profe)
  administrativo_1.altaProfesor()
  print(ITBA.profesores)
  print(ITBA.legajos_profesores)

  # print("Negocios")
  # print(licnegocios.alumnos_actuales)
  # print("Analitica")
  # print(licnanalitica.alumnos_actuales)
  # print("Ingenieria Industrial")
  # print(ingindustrial.alumnos_actuales)
  # print("Ingenieria Informatica")
  # print(inginformatica.alumnos_actuales)

  print("-----------")
  print(len(administrativo_1.tramites_abiertos))
  print()
  # print(len(administrativo_2.tramites_abiertos))
  # print(len(administrativo_3.tramites_abiertos))