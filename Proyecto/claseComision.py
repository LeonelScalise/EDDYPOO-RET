class Comision:
    def __init__(self, codigo_comision, aula, profesor,materia, dia_y_horario = {}):
        self.codigo_comision = codigo_comision
        self.aula = aula
        self.profesor = profesor
        self.materia=materia
        self.ayudantes = []
        self.dia_y_horario = dia_y_horario
        self.alumnos = []