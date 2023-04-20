from clasePersona import *

class Institucion():
    def __init__(self, nombre, rector) -> None:
        self.nombre = nombre
        self.sedes = []
        self.rector = rector
        self.carreras = []
        self.alumnos = []
        self.profesores = []
        self.administrativos = []
    
    def buscar_alumno(self, legajo):
        for alumno in self.alumnos:
            if legajo == alumno.legajo:
                return alumno
        
    
    def agregar_alumno(self, alumno):
        
        self.alumnos.append(alumno)
        print("Alumno agregado")


            
""" 
    def buscar_profesor(legajo):

    
    def buscar_administrativo(legajo): """



if __name__=="__main__":

    ITBA = Institucion("ITBA", "Pepe")

    Leo = Alumno("leonel",4344893,"M","fecha","Legajo de leo",[],[],"fecha","negocios","vigente")
    Fede = Alumno("fede",4112893,"M","fecha","Legajo de fede",[],[],"fecha","negocios","vigente")

    ITBA.agregar_alumno(Leo)
    ITBA.agregar_alumno(Fede)
    
    print(ITBA.buscar_alumno("Legajo de leo"))

    