from claseInstitucion import *
from clasePersona import Alumno, Profesor, Administrativo
from popularInstitucion import ITBA
<<<<<<< HEAD
from claseCarrera import *
from claseMateria import *


Lic_negocios = Carrera("Licenciatura en Gestión de Negocios", "Luis Paolini")

Leo = Alumno("Leonel Scalise",43046873,"M","fecha",62523,[],[],"fecha",Lic_negocios,"vigente")
Juana = Alumno("Juana Santacreu",4112893,"F","fecha",23424,[],[],"fecha",Lic_negocios,"vigente")
Mati = Alumno("Matías Díaz Cantón",43573875,"M","fecha",62473,[],[],"fecha",Lic_negocios,"vigente")
=======
from popularCarrera import *

Leo = Alumno("Leonel Scalise","43046873","M","fecha",62523,"fecha",licnegocios,"Activo")
Juana = Alumno("Juana Santacreu","4112893","F","fecha",23424,"fecha",licnegocios,"Activo")
Mati = Alumno("Matías Díaz Cantón","43573875","M","fecha",62473,"fecha",licnegocios,"Activo")
>>>>>>> f5c2483c238d8afc598041aac88e307d02f99351

Girafa = Profesor("Profe Girafale", "23123141", "M", "12/12/12", "PR10000", "11/12/12")  #(nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, fecha_baja=None, comisiones_acargo=None

<<<<<<< HEAD
ElAdmin = Administrativo("El Admin",41741,"M","fecha",10000,"FECHA INGRESO")  # nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, tramites_abiertos, tramites_resueltos, fecha_baja=None

Analisis_matematico = Materia("55.22", "Analisis matematico", 3, "SDT", "Matematica", "Noni")
Algebra = Materia("67.30", "Algebra", 6, "SDF", "Matematica", "Neli")
Microeconomia = Materia("43.74", "Microeconomia", 6, "SDF", "Economia", "Pablito", [Analisis_matematico, Algebra])

=======
ElAdmin = Administrativo("El Admin","4174123123","M","fecha","AD10000","FECHA INGRESO")  # nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, tramites_abiertos, tramites_resueltos, fecha_baja=None
 
>>>>>>> f5c2483c238d8afc598041aac88e307d02f99351

ITBA.agregar_alumno(Leo)
ITBA.agregar_alumno(Juana)
ITBA.agregar_alumno(Mati)

ITBA.agregar_profesor(Girafa)

ITBA.agregar_administrativo(ElAdmin)

<<<<<<< HEAD
Lic_negocios.agregar_materia(Analisis_matematico)
Lic_negocios.agregar_materia(Algebra)
Lic_negocios.agregar_materia(Microeconomia)
=======
Leo.iniciarTramite(ITBA)
Leo.iniciarTramite(ITBA)
Leo.iniciarTramite(ITBA)
ITBA.agregar_carrera(licnegocios)
ITBA.agregar_carrera(licnanalitica)
ITBA.agregar_carrera(ingindustrial)
ITBA.agregar_carrera(inginformatica)
>>>>>>> f5c2483c238d8afc598041aac88e307d02f99351
