#Elegir las Clases
#Relacion entre clases
#Como almacenar la info dentro de cada clase --> listas o vectores / listas enlazadas / Diccionarios
#Diseño de menu en la TERMINAL

class Persona:
    def __init__(self, nombre, apellido, dni, numero_legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numero_legajo = numero_legajo

class Profesor(Persona):
    def __init__(self, nombre, apellido, dni, numero_legajo, codigo, email):
        super().__init__(nombre, apellido, dni, numero_legajo)
        self.codigo = codigo
        self.email = email

class Estudiante(Persona):
    def __init__(self, nombre, apellido, dni, numero_legajo, carrera, matriculado, sede):
        super().__init__(nombre, apellido, dni, numero_legajo)
        self.carrera = carrera
        self.matriculado = matriculado
        self.sede = sede

    def __str__(self):
        return f"{super().__str__()} - {self.carrera} - {self.sede}"

    def agregar_materia(self, materia, comision):
        if materia not in self.materias:
            if comision.agregar_alumno(self):
                self.materias.append(materia)
                return True

class Materia:
    def __init__(self, codigo, nombre, creditos, sede, aula):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.sede = sede
        self.aula = aula
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    def agregar_comision(self, codigo, vacantes, profesor):
        comision = Comision(codigo, vacantes, profesor)
        self.comisiones.append(comision)

class Comision:
    def __init__(self, codigo, vacantes, profesor, dia, hora_inicio, hora_fin, alumnos=[]):
        self.codigo = codigo
        self.vacantes = vacantes
        self.profesor = profesor
        self.alumnos = alumnos
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def __str__(self):
        return f"{self.codigo} - {self.profesor}"

    def agregar_alumno(self, alumno):
        if len(self.alumnos) < self.vacantes:
            self.alumnos.append(alumno)
            return True
        else:
            return False

class Dia_Horario:
    def __init__(self, dia, horario):
        self.dia = dia
        self.horario = horario




