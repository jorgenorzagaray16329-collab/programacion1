import modelos.curso
from modelos.curso import agregarCurso
from modelos.alumno import agregarAlumno

cursos={}

nombre = input("Nombre de tu curso nuevo")
cursonuevo = agregarCurso()
cursos[nombre] = cursonuevo
idAlumno = input("Dame el id del Alumno")
nuevoAlumno = agregarAlumno()
cursos[nombre]["Alumnos"][idAlumno] = nuevoAlumno
