class Persona:
  def _init_(self, nombre_apellido, dni, sexo, fecha_nac)
  self.nombre_apellido = nombre_apellido
  self.dni = dni
  self.sexo = sexo
  self.fecha_nac = fecha_nac

class Alumno(Pesrona):
  def _init_(self, legajo, materias_aprobadas, materias_en_curso, fecha_ingreso, carrera, estado_alumno, creditos_aprobados=0)
  self.legajo = legajo
  self.materias_aprobadas = []
  self.materias_en_curso = []
  self.fecha_ingreso = fecha_ingreso
  self.carrera = carrera
  self.estado_alumno = estado_alumno
  self.tramites_pendientes = []
  self.tramites_resueltos = []
  self.legajo_alumnos = []



class Profesor(Persona):
  def _init_(self, legajo, fecha_ingreso, fecha_baja=None, comisiones_acargo=None)
  self.legajo = legajo
  self.fecha_ingreso = fecha_ingreso
  self.fecha_baja = fecha_baja
  self.comisiones_acargo = []  
