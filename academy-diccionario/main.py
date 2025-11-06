import modelos.curso as curso
from modelos.curso import agregarCurso
from modelos.alumno import agregarAlumno

cursos={}
#Agregar Curso
#Modificar Curso
#Agregar alumno a curso
#dar de baja alumno
#mostrar listado de alumnos de un curso
#salir


nombre = input("Nombre de tu curso nuevo")
cursonuevo = agregarCurso()
cursos[nombre] = cursonuevo
idAlumno = input("Dame el id del Alumno")
nuevoAlumno = agregarAlumno()
cursos[nombre]["Alumnos"][idAlumno] = nuevoAlumno
