from claseInstitucion import *
from clasePersona import Alumno, Profesor, Administrativo
from popularInstitucion import ITBA
from claseCarrera import *
from claseMateria import *


Lic_negocios = Carrera("Licenciatura en Gestión de Negocios", "Luis Paolini")

Leo = Alumno("Leonel Scalise",43046873,"M","fecha",62523,[],[],"fecha",Lic_negocios,"vigente")
Juana = Alumno("Juana Santacreu",4112893,"F","fecha",23424,[],[],"fecha",Lic_negocios,"vigente")
Mati = Alumno("Matías Díaz Cantón",43573875,"M","fecha",62473,[],[],"fecha",Lic_negocios,"vigente")

Girafa = Profesor("Profe Girafale", 23, "M", "12/12/12", 35351, "11/12/12")  #(nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, fecha_baja=None, comisiones_acargo=None

ElAdmin = Administrativo("El Admin",41741,"M","fecha",10000,"FECHA INGRESO")  # nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, tramites_abiertos, tramites_resueltos, fecha_baja=None

Analisis_matematico = Materia("55.22", "Analisis matematico", 3, "SDT", "Matematica", "Noni")
Algebra = Materia("67.30", "Algebra", 6, "SDF", "Matematica", "Neli")
Microeconomia = Materia("43.74", "Microeconomia", 6, "SDF", "Economia", "Pablito", [Analisis_matematico, Algebra])


ITBA.agregar_alumno(Leo)
ITBA.agregar_alumno(Juana)
ITBA.agregar_alumno(Mati)

ITBA.agregar_profesor(Girafa)

ITBA.agregar_administrativo(ElAdmin)

Lic_negocios.agregar_materia(Analisis_matematico)
Lic_negocios.agregar_materia(Algebra)
Lic_negocios.agregar_materia(Microeconomia)