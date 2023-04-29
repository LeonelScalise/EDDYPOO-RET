from claseInstitucion import *
from clasePersona import Alumno,Profesor,Administrativo,Persona
from popularInstitucion import ITBA
from popularCarrera import *

Leo = Alumno("Leonel Scalise","43046873","M","fecha",62523,"fecha",licnegocios,"Activo")
Juana = Alumno("Juana Santacreu","4112893","F","fecha",23424,"fecha",licnegocios,"Activo")
Mati = Alumno("Matías Díaz Cantón","43573875","M","fecha",62473,"fecha",licnegocios,"Activo")

Girafa = Profesor("Profe Girafale", "23123141", "M", "12/12/12", "PR10000", "11/12/12")  #(nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, fecha_baja=None, comisiones_acargo=None

ElAdmin = Administrativo("El Admin","4174123123","M","fecha","AD10000","FECHA INGRESO")  # nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, tramites_abiertos, tramites_resueltos, fecha_baja=None
 

ITBA.agregar_alumno(Leo)
ITBA.agregar_alumno(Juana)
ITBA.agregar_alumno(Mati)

ITBA.agregar_profesor(Girafa)

ITBA.agregar_administrativo(ElAdmin)

Leo.iniciarTramite(ITBA)
Leo.iniciarTramite(ITBA)
Leo.iniciarTramite(ITBA)
ITBA.agregar_carrera(licnegocios)
ITBA.agregar_carrera(licnanalitica)
ITBA.agregar_carrera(ingindustrial)
ITBA.agregar_carrera(inginformatica)
