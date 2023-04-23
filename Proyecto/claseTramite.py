class Tramite():
    def __init__(self, id, alumno, administrativo, tipo_de_tramite, fecha_de_inicio, estado="Pendiente", comision=None):
        self.id = id
        self.alumno = alumno
        self.administrativo = administrativo
        self.tipo_de_tramite = tipo_de_tramite
        self.fecha_de_inicio = fecha_de_inicio
        self.estado = estado
        self.comision = comision
        self.tramites_resueltos = []
        self.tramites_abierto = []