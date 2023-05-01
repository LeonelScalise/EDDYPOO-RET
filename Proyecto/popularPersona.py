from claseInstitucion import *
from clasePersona import Alumno, Profesor, Administrativo
from popularInstitucion import ITBA
from popularCarrera import *
from claseMateria import *
from claseComision import *

ITBA.agregar_carrera(licnegocios)
ITBA.agregar_carrera(licnanalitica)
ITBA.agregar_carrera(ingindustrial)
ITBA.agregar_carrera(inginformatica)

Leo = Alumno("Leonel Scalise","43046873","M","fecha",62523,"fecha","Activo",licnegocios)
Juana = Alumno("Juana Santacreu","4112893","F","fecha",23424,"fecha","Activo",licnegocios)
Mati = Alumno("Matías Díaz Cantón","43573875","M","fecha",62473,"fecha","Activo",licnegocios)

Girafa = Profesor("Profe Girafale", "23123141", "M", "12/12/12", "PR10000", "11/12/12")  #(nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, fecha_baja=None, comisiones_acargo=None

ElAdmin = Administrativo("El Admin","41741232","M","fecha","AD10000","FECHA INGRESO")  # nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, tramites_abiertos, tramites_resueltos, fecha_baja=None

Analisis_matematico = Materia("55.22", "Analisis matematico", 3, "SDT", "Matematica")
Algebra = Materia("67.30", "Algebra", 6, "SDF", "Matematica")
Microeconomia = Materia("43.74", "Microeconomia", 6, "SDF", "Economia", [Analisis_matematico, Algebra])

comi1 = Comision("A", "201F", Girafa, {"dia":["Lunes"], "horario":["12:30-14:30"]})
comi2 = Comision("B", "202F", Girafa, {"dia":["Lunes"], "horario":["12:30-14:30"]})

Analisis_matematico.comisiones.append(comi1)
Analisis_matematico.comisiones.append(comi2)

ITBA.agregar_alumno(Leo)
ITBA.agregar_alumno(Juana)
ITBA.agregar_alumno(Mati)

ITBA.agregar_profesor(Girafa)

ITBA.agregar_administrativo(ElAdmin)

licnegocios.agregar_materia(Analisis_matematico)
licnegocios.agregar_materia(Algebra)
licnegocios.agregar_materia(Microeconomia)

# Leo.iniciarTramite(ITBA)
# Leo.iniciarTramite(ITBA)
# Leo.iniciarTramite(ITBA)

# Analisis_matematico.crearComision()
# print(Analisis_matematico.comisiones)
