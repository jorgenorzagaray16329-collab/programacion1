import tkinter as tk
from tkinter import ttk #Themed Tkinter

def saludar():
    etiqueta2.config(text="Hola, "+entrada_texto.get())


#1. Crear la ventana principal
root = tk.Tk()
root.title("Mi primer ventana (Raiz)")
root.geometry("800x600") #WxH Ancho x Alto

#2. Ponemos los widgets
etiqueta = ttk.Label(root,text="Nombre:", font="Helvetica 20")
etiqueta.grid(row=0,column=0, padx=20,pady=20)

entrada_texto = ttk.Entry(root,font="Helvetica 20")
entrada_texto.grid(row=0,column=1, padx=10,pady=20)

etiqueta2 = ttk.Label(root,font="Helvetica 30"
                      ,background="#0099CC"
                      ,foreground="#f2f2f2")
etiqueta2.grid(row=1, column=0, columnspan=2)

boton = ttk.Button(root, 
                    text="Esto es un boton"                    
                    , padding=10)
boton.config(command=saludar)
boton.grid(row=2,column=0,columnspan=2 , padx=20,pady=20)
#boton.pack(pady=20)
#boton.place(x=100,y=200)

check = ttk.Checkbutton(
    root,
    text="Aceptas los Terminos?"
    
)

check.grid(row=3,column=0,columnspan=2)

opcion = tk.StringVar()
opcion.set("Rojo")

r1= ttk.Radiobutton(root,text="Rojo",variable=opcion,value="Rojo")
r2= ttk.Radiobutton(root,text="Verde",variable=opcion,value="Verde")
r3= ttk.Radiobutton(root,text="Azul",variable=opcion,value="Azul")

r1.grid(row=4,column=0)
r2.grid(row=4,column=1)
r3.grid(row=4,column=2)



#3. Siempre va al final
root.mainloop() # Mantener activa la ventana y escuchando eventos


