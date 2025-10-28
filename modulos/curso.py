def agregar():
    nombre = input("Digite el nombre del curso").title()
    instructor = input("Digite el nombre del instructor")
    aula = input("Digite el aula")
    alumnos=[]
    curso = [nombre,instructor,aula,alumnos]
    return curso

def eliminar(cursos,idCurso):
    return cursos

def listado(cursos):
    print("cursos")