#Crear una funcion para centrar la ventana.

def centrar_ventana(ventana,ancho,alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = int( (pantalla_ancho/2) - (ancho/2) )#Determina el centro de la pantalla horizantalmente
    y = int((pantalla_alto/2) - (alto/2) ) #Determina el centro de la pantalla verticalmente
    return ventana.geometry(f"{ancho}x{alto}+{x}+{y}") #WxH+X+Y