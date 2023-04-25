from claseInstitucion import *
from clasePersona import Alumno,Profesor,Administrativo,Persona
from popularInstitucion import ITBA

Leo = Alumno("Leonel Scalise",43046873,"M","fecha",62523,[],[],"fecha","negocios","vigente")
Juana = Alumno("Juana Santacreu",4112893,"F","fecha",23424,[],[],"fecha","negocios","vigente")
Mati = Alumno("Matías Díaz Cantón",43573875,"M","fecha",62473,[],[],"fecha","negocios","vigente")

Girafa = Profesor("Profe Girafale", 23, "M", "12/12/12", 35351, "11/12/12")  #(nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, fecha_baja=None, comisiones_acargo=None

ElAdmin = Administrativo("El Admin",41741,"M","fecha",10000,"FECHA INGRESO")  # nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, tramites_abiertos, tramites_resueltos, fecha_baja=None
 

ITBA.agregar_alumno(Leo)
ITBA.agregar_alumno(Juana)
ITBA.agregar_alumno(Mati)

ITBA.agregar_profesor(Girafa)

ITBA.agregar_administrativo(ElAdmin)

Leo.iniciarTramite(ITBA)
Leo.iniciarTramite(ITBA)
Leo.iniciarTramite(ITBA)
