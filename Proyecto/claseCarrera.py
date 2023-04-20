class Carrera():
    def __init__(self,nombre,creditos_para_recibirse,director_carrera):
        self.nombre = nombre
        self.creditos_para_recibirse = creditos_para_recibirse
        self.director_carrera = director_carrera
        self.alumnos_actuales = []
        self.alumnos_recibidos = []
        self.cantidad_alumnos_recibidos=0
    def __str__(self):
        return "La carrera {} tiene de director a {} y necesita {} creditos para recibirse".format(self.nombre,self.director_carrera,self.creditos_para_recibirse)
