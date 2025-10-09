#Esto es un comentario y no es interpretado en la ejecución

#Ejemplo del uso de print()
print("Hola mundo desde Python")

numero = 10+5
variable_prueba = "Hola variable"
variablePruebaJoroba = "Camello" #Notación camello porque simula unas jorobas


#type()  me muestra el tipo de dato de la variable
print(type(numero))
print(type(variable_prueba))
print(type(variablePruebaJoroba))

#input(<texto>) solicita al usuario una entrada de datos y retorna un str
edad = input("Dime tu edad.")
edad = int(edad)
print(edad)
print(type(edad))