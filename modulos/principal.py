import alumno
import curso
cursos= []

nuevoCurso = curso.agregar()
cursos.append(nuevoCurso)
nuevoCurso = curso.agregar()
cursos.append(nuevoCurso)
nuevoCurso = curso.agregar()
cursos.append(nuevoCurso)

for i in range(len(cursos)):
    print(f"{i} <==> {cursos[i][0]}")

opcion = int(input("Digite el indice del curso"))

for alumno in cursos[opcion][3]:
    print(alumno)

cursos[opcion][3].append(input("Digita el nombre del alumno"))