class Materia:
    def init(self, codigo_materia, nombre, creditos, sede, departamento, titular, correlativas=[]):
        self.codigo_materia = codigo_materia
        self.nombre = nombre
        self.creditos = creditos
        self.sede = sede
        self.departamento = departamento
        self.titular = titular
        self.correlativas = correlativas
        self.comisiones = []

    def str(self):
        return f"{self.codigo_materia} - {self.nombre}"
    

