class Comision:
    def init(self, codigo_comision, aula, profesor, ayudantes=[], dia_y_horario = {}, alumnos=[]):
        self.codigo_comision = codigo_comision
        self.aula = aula
        self.cupos = aula.capacidad
        self.profesor = profesor
        self.ayudantes = ayudantes
        self.dia_y_horario = dia_y_horario
        self.alumnos = alumnos