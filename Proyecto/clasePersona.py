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
from validadorNota import *
import matplotlib.pyplot as plt



clear = lambda : os.system('cls')

class Persona:
  def __init__(self, nombre_apellido, dni, sexo, fecha_nac):
    while not str(dni).isdigit():
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
          return armado_menu(f"Bienvenid{x} {alumno.nombre_apellido}", ["Inscripcion a materias", "Iniciar Tramite", "Volver"], [lambda : alumno.displayMateriasDisponibles(), lambda : alumno.iniciarTramite(ITBA)])


  def __init__(self, nombre_apellido, dni, sexo, fecha_nac, legajo,fecha_ingreso,estado_alumno="Activo", carrera=None, creditos_aprobados=0):
    super().__init__(nombre_apellido, dni, sexo, fecha_nac)
    self.legajo = legajo
    self.materias_aprobadas = []
    self.materias_en_curso = []
    self.fecha_ingreso = fecha_ingreso
    self.carrera = carrera
    self.historial_academico = {}
    self.estado_alumno = estado_alumno
    self.tramites_pendientes = []
    self.tramites_resueltos = []

 
  def __str__(self):
    return self.nombre_apellido
  

  def iniciarTramite(self,institucion):
    id_tramite = 0

    if len(institucion.historial_tramites) != 0:
      id_tramite= institucion.historial_tramites[-1].id + 1
    tipo_de_tramite = input("Ingrese el motivo del tramite: ")
    cantidad_administrativos = len(institucion.administrativos)
    i_random = random.randint(0,cantidad_administrativos-1)
    administrativo_asignado=institucion.administrativos[i_random]
    nuevo_tramite = Tramite(id_tramite,self,administrativo_asignado,tipo_de_tramite,"24/4/2023")
    administrativo_asignado.tramites_abiertos.append(nuevo_tramite)
    institucion.tramites_abiertos.append(nuevo_tramite)
    institucion.historial_tramites.append(nuevo_tramite) 
    return print("Ya iniciaste el tramite")

  def inscribirMateria(self, materia):
    contador = 0
    print(f"\t\t\nComisiones disponibles para incripcion en {materia.nombre}\n")
    for comisiones in materia.comisiones:
      contador += 1
      print(("{}. {}: {}").format(contador, comisiones.codigo_comision, comisiones.dia_y_horario))
    opcion_elegida = validador(contador)
    comision = materia.comisiones[opcion_elegida - 1]
    comision.alumnos.append(self)
    print(comision.alumnos[0].nombre_apellido)
    materia.alumnos.append(comision.alumnos[-1])
    self.materias_en_curso.append(materia)
    clear()
    print(f"Te has inscripto correctamente a la comision {comision.codigo_comision} de la materia {materia.nombre}")

  def displayMateriasDisponibles(self):
    materias_disponibles = []
    c1 = 0
    c2 = 0
    print(f"\t\t\nMaterias disponibles para incripcion de {self.nombre_apellido}\n")
    for materia in self.carrera.materias:
      if len(materia.correlativas) != 0:
        for corre in materia.correlativas:
          if corre in self.materias_aprobadas:
            c1 += 1 #sirve para verificar si es igual a la cantidad de correlativas que tiene la materia, eso querría decir que tiene todas las correlativas aprobadas
        if c1 == len(materia.correlativas) and materia not in self.materias_aprobadas and materia not in self.materias_en_curso:
            materias_disponibles.append(materia)
      elif materia not in self.materias_aprobadas and materia not in self.materias_en_curso:
        materias_disponibles.append(materia)

    for materia in materias_disponibles:
      c2 += 1
      print(("{}. {} {}").format(c2, materia.codigo_materia, materia.nombre))
    opcion_elegida = validador(c2)
    clear()
    self.inscribirMateria(materias_disponibles[opcion_elegida - 1])
        

class Profesor(Persona):
  def menu_registro_profesor(institucion:Institucion):
    x = "o"
    legajo_ingresado = validadorLegajoAdminyProf(institucion, 'prof')
    clear()
    for prof in institucion.profesores:
        if prof.legajo == legajo_ingresado:
          if prof.sexo == "F":
            x = "a"
          return armado_menu(f"Bienvenid{x} {prof.nombre_apellido}", ["Subir nota final", "Iniciar Tramite", "Volver"], [lambda : prof.displayMateriasActivas(), lambda: prof.iniciarTramite(ITBA)])


  def __init__(self, nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, fecha_baja=None, comisiones_a_cargo=None):
    super().__init__(nombre_apellido, dni, sexo, fecha_nac)
    self.legajo = legajo
    self.fecha_ingreso = fecha_ingreso
    self.fecha_baja = fecha_baja
    self.comisiones_a_cargo = []

  def iniciarTramite(self,institucion):
    id_tramite = 0

    if len(institucion.historial_tramites) != 0:
      id_tramite= institucion.historial_tramites[-1].id + 1
    tipo_de_tramite = input("Ingrese el motivo del tramite: ")
    cantidad_administrativos = len(institucion.administrativos)
    i_random = random.randint(0,cantidad_administrativos-1)
    administrativo_asignado=institucion.administrativos[i_random]
    nuevo_tramite = Tramite(id_tramite,self,administrativo_asignado,tipo_de_tramite,"24/4/2023")
    administrativo_asignado.tramites_abiertos.append(nuevo_tramite)
    institucion.tramites_abiertos.append(nuevo_tramite)
    institucion.historial_tramites.append(nuevo_tramite) 
    return print("Ya iniciaste el tramite")
  
  def subirNotaFinal(self, materia):
    comisiones_a_cargo = []
    contador = 0
    print("Seleccione la comision a la que desea subir la nota final:\n")
    for comision in materia.comisiones:
      if self == comision.profesor:
        comisiones_a_cargo.append(comision)
    
    for comision in comisiones_a_cargo:
      contador += 1
      print(("{}. Comision {} de {}").format(contador, comision.codigo_comision, materia.nombre))

    opcion_elegida = validador(contador)
    comision_elegida = comisiones_a_cargo[opcion_elegida - 1]
    clear()

    contador = 0
    print("Seleccione el alumno al que desea subir la nota final:\n")
    if len(comision_elegida.alumnos) != 0:
      for alumno in comision_elegida.alumnos:
        contador += 1
        print(("{}. {}").format(contador, alumno.nombre_apellido))
      opcion_elegida = validador(contador)
      clear()
      alumno_elegido = comision_elegida.alumnos[opcion_elegida - 1]
      Nota_final = validadorNota()
      alumno_elegido.historial_academico[materia.nombre] = Nota_final
      if Nota_final > 4:
        alumno_elegido.materias_aprobadas.append(materia)
        print(f"La nota final se cargó correctamente. {alumno_elegido} aprobó {materia.nombre}")
      else:
        print(f"La nota final se cargó correctamente. {alumno_elegido} no aprobó {materia.nombre}")
    else:
      print("No hay alumnos en esta comision")
  
  def displayMateriasActivas(self):
    contador = 0
    materias_activas = []
    print("Materias a las que está inscripto\n")
    for carrera in ITBA.carreras:
      for materia in carrera.materias:
        if self in materia.profesores:
          materias_activas.append(materia)
    for materia in materias_activas:
      contador += 1
      print(("{}. {} {}").format(contador, materia.codigo_materia, materia.nombre))
    opcion_elegida = validador(contador)
    clear()
    self.subirNotaFinal(materias_activas[opcion_elegida - 1])

class Administrativo(Persona):
  def altaAdministrativo(institucion:Institucion):
        
        nombre_apellido = input("Ingrese el nombre y apellido del administrativo: ")
        dni = input("Ingrese el DNI del empleado: ")
        fecha_nac = input("Ingrese la fecha de nacimiento: ")
        sexo = input("Ingrese el sexo: ")
        if len(ITBA.legajos_administrativos) != 0:
          legajo_numero = int(ITBA.legajos_administrativos[-1][2:])+1
          legajo_alfa = "AD"
          legajo = legajo_alfa + str(legajo_numero)
        else:
          legajo="AD10000"
        fecha_ingreso = input(f'Ingrese la fecha de ingreso a {institucion.nombre}: ')

        institucion.administrativos.append(Administrativo(nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso))
        institucion.legajos_administrativos.append(legajo)
        print(f'El administrativo {nombre_apellido} se ha creado correctamente')
        print(len(institucion.administrativos))

  def menu_registro_administrativo(institucion:Institucion):
    x = "o"
    legajo_ingresado = validadorLegajoAdminyProf(institucion)
    clear()
    for admin in institucion.administrativos:
        if admin.legajo == legajo_ingresado:
          if admin.sexo == "F":
            x = "a"
          return armado_menu(f"Bienvenid{x} {admin.nombre_apellido}", ["Dar de alta alumno", "Dar de baja alumno", "Dar de alta profesor", "Dar de baja profesor", "Tramites","Crear Comisión", "Asignar profesor a materia", "Desasignar profesor a materia","Distribución de alumnos por carrera", "Volver"], [lambda : admin.altaAlumno(), lambda : admin.bajaAlumno(), lambda : admin.altaProfesor(), lambda : admin.bajaProfesor(), lambda : admin.displayTramiteActivo(), lambda:admin.crearComision(), lambda : admin.asignarProfesor(), '', lambda : admin.alumnos_actualesxCarrera()])
        
  def __init__(self, nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, fecha_baja=None):
    super().__init__(nombre_apellido, dni, sexo, fecha_nac)
    self.legajo = legajo
    self.fecha_ingreso = fecha_ingreso
    self.fecha_baja = fecha_baja
    self.tramites_abiertos = []
    self.tramites_resueltos = []
    self.fecha_baja = fecha_baja

  
  def asignarProfesor(self):
    contador = 0
    flag = False
    legajo_profesor = validadorLegajoAdminyProf(ITBA,"prof")
    materias_disponibles = []
    for profesor in ITBA.profesores:
      if profesor.legajo == legajo_profesor:
        profesor_elegido = profesor
        clear()
    print("Materias a las que se lo puede asignar\n")
    for carrera in ITBA.carreras:
      for materia in carrera.materias:
        if len(materia.comisiones) > 0:
          for comision in materia.comisiones:
            if comision.profesor == None:
              flag = True
        if flag:
          contador += 1
          materias_disponibles.append(materia)
          print(("{}. {} {}").format(contador, materia.codigo_materia, materia.nombre))
          flag = False

    if len(materias_disponibles) == 0:
      print("Todas las materias tienen un profesor asignado")
    else:
      opcion_elegida1 = validador(contador)
      materia_elegida = materias_disponibles[opcion_elegida1 - 1]
      clear()
      
      print(f"Comisiones de {materia_elegida.nombre} a las que se lo puede asignar\n")
      contador = 0
      for comision in materia_elegida.comisiones:
        if comision.profesor == None:
          contador += 1
          print(("{}. Comision {} de {}").format(contador, comision.codigo_comision, materia_elegida.nombre))

      opcion_elegida2 = validador(contador)
      comision_elegida = materia_elegida.comisiones[opcion_elegida2 - 1]

      comision_elegida.profesor = profesor_elegido
      materia_elegida.profesores.append(profesor_elegido)

      print(f"Se ha asignado correctamente a {profesor_elegido.nombre_apellido} a la comision {comision_elegida.codigo_comision} de {materia_elegida.nombre}")

  
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
    contador=0
    

    alumno_nuevo = Alumno(nombre,dni,sexo,fecha_nacimiento,legajo,fecha_ingreso)
    clear()
    #Para que el administrativo anote al alumno en un objeto carrera
    print(f'\n\t\t Ingrese la carrera del alumno\n')
    for carrera in ITBA.carreras:
      contador += 1
      print(("{}. {}").format(contador,carrera.nombre))
    opcion_elegida = validador(contador)
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
    if len(ITBA.legajos_profesores) != 0:
      legajo_numero = int(ITBA.legajos_profesores[-1][2:])+1
      legajo_alfa = "PR"
      legajo = legajo_alfa + str(legajo_numero)
    else:
      legajo="PR10000"
    fecha_ingreso = input("Ingrese la fecha de ingreso del profesor: ")

    profesor_nuevo = Profesor(nombre, dni, sexo, fecha_nacimiento, legajo, fecha_ingreso)
    ITBA.agregar_profesor(profesor_nuevo)

  def bajaAlumno(self):
    legajo_alumno = validadorLegajoAlumnos(ITBA)
    for alumno in ITBA.alumnos:
      if alumno.legajo == legajo_alumno:
        print(ITBA.alumnos)
        ITBA.alumnos.remove(alumno)
        print(ITBA.alumnos)
        print(alumno.carrera.alumnos_actuales)
        alumno.carrera.alumnos_actuales.remove(alumno)
        print(alumno.carrera.alumnos_actuales)


  def bajaProfesor(self):
    flag = False
    legajo_profesor = validadorLegajoAdminyProf(ITBA,"prof")
    clear()
    for profesor in ITBA.profesores:
      if profesor.legajo == legajo_profesor:
        profesor_elegido = profesor
    for carrera in ITBA.carreras:
      for materia in carrera.materias:
        if len(materia.comisiones) != 0:
          for comision in materia.comisiones:
            if legajo_profesor == comision.profesor.legajo:
              flag = True
              comision.profesor = None
              print(f"Se ha dado de baja al profesor {profesor_elegido.nombre_apellido} de la Comision {comision.codigo_comision} de la Materia {materia.nombre}")
        
        if flag:
          materia.profesores.remove(profesor_elegido)
          flag = False
      
    ITBA.profesores.remove(profesor_elegido)
      
  
  def crearComision(self):
    contador = 0
    materias_total = []
    print("Materias de la institución\n")
    for carrera in ITBA.carreras:
      for materia in carrera.materias:
        contador += 1
        materias_total.append(materia)
        print(("{}. {} {}").format(contador, materia.codigo_materia, materia.nombre))
    
    opcion_elegida = validador(contador)
    materia_elegida = materias_total[opcion_elegida - 1]
    clear()
    cod_comi = "A"
    if len(materia_elegida.comisiones) != 0:
      cod_comi = ascii_uppercase[len(materia_elegida.comisiones)]

    print(f"Creación de la comision para {materia_elegida.nombre}\n")
    aula = input("Ingrese el aula de la Comisión: ")
    profesor_asignado = validadorLegajoAdminyProf(ITBA,"prof")
    dia = input("Ingrese el/los dia/s de la semana separados por (,): ").upper().replace(" ","").split(",")
    horario = input("Ingrese el/los horario/s respectivamente a los dias ingresados previamente.(Ejemplo: 10:30 - 12:40): ").replace(" ","").split(",")
    dia_horario = {"Dia":dia,"Horario":horario}
    clear()
    
    nueva_comision = Comision(cod_comi, aula, profesor_asignado, dia_horario)

    materia_elegida.comisiones.append(nueva_comision)
    materia_elegida.profesores.append(profesor_asignado)

    print(f"La comision {nueva_comision.codigo_comision} de {materia_elegida.nombre} fue creada correctamente ")


  def alumnos_actualesxCarrera(self):
   alumnos=[]
   carreras=[]
   for carrera in ITBA.carreras:
     c=0
     carreras.append(carrera.nombre)
     for alumno in carrera.alumnos_actuales:
       c+=1
     alumnos.append(c)
   plt.pie(alumnos,labels=carreras,autopct='%1.1f%%')
   plt.title(label="Alumnos por Carrera")
   plt.show()
  
  


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