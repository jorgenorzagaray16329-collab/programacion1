import tkinter as tk
from tkinter import font,filedialog, messagebox
from config import TITULO,COLOR_BARRA_SUPERIOR,COLOR_MENU_LATERAL,COLOR_PANEL_PRINCIPAL
from util.util_ventana import centrar_ventana,cargar_fuente_memoria, resolver_ruta
from util.util_imagenes import leer_imagen
import pygame
import os

#python -m PyIntaller --noconsole --onefile 
# --icon="./imagenes/sales.ico" --name="Mi Punto de Venta"
# --add-data "imagenes;imagenes"
# --add-data "fuentes;fuentes"
# main.py

ruta=""
estado=""
nombre_archivo="<No se ha seleccionado un archivo>"

def bind_hover_events(button):
    button.bind("<Enter>", lambda event:on_enter(event,button))
    button.bind("<Leave>",lambda event:on_leave(event,button))

def on_enter(event,button):
    button.config(bg="#0099CC")

def on_leave(event,button):
    button.config(bg=COLOR_MENU_LATERAL)

def toggle_panel():
    if menu_lateral.winfo_ismapped():
        menu_lateral.pack_forget()
    else:
        menu_lateral.pack(side=tk.LEFT, fill="y")

def limpiar_panel(panel):
    for widget in panel.winfo_children():
        widget.destroy()

def mostrar_inicio():
    limpiar_panel(panel_principal)
    label_imagen_principal = tk.Label(panel_principal,text="Inicio")
    label_imagen_principal.pack()

def mostrar_ventas():
    limpiar_panel(panel_principal)
    label_ventas = tk.Label(panel_principal,text="Ventas")
    label_ventas.pack()

def cargar_cancion():
    global ruta
    ruta = filedialog.askopenfilename(title="Elige un mp3"
                        ,filetypes=[("Archivos MP3","*.mp3")])
    if ruta:
        global nombre_archivo
        nombre_archivo = os.path.basename(ruta)
        label_musica.config(text=nombre_archivo)
    
def reproducir():
    global ruta
    global estado
    if ruta:
        try:
            if estado=="pause":
                #Si estaba pausado , le quitamos el pause
                pygame.mixer.music.unpause()
                estado="play"
            else:
                estado= "play"
                pygame.mixer.music.load(ruta)
                pygame.mixer.music.play()
        except Exception as e:
            messagebox.showerror("Error"
                                 ,f"No se pudo reproducir el archivo {e}")
    else:
        messagebox.showwarning("Atencion"
                               ,"Primero debes cargar una canción")


def pausar():
    pygame.mixer.music.pause()
    global estado
    estado = "pause"

def detener():
    pygame.mixer.music.stop()
    global estado
    estado = "stop"

def cambiar_volumen(valor):
    #El volumnen va de 0 a 1 
    pygame.mixer.music.set_volume(float(valor)/100)
    return "volumen"

def salir():
    root.destroy()


#Cargar la fuentes.
cargar_fuente_memoria("./fuentes/Font Awesome 7 Brands-Regular-400.otf")
cargar_fuente_memoria("./fuentes/Font Awesome 7 Free-Regular-400.otf")
cargar_fuente_memoria("./fuentes/Font Awesome 7 Free-Solid-900.otf")

#Inicializar pygame
pygame.init()

root = tk.Tk()
root.title(TITULO)
rutaIcono = resolver_ruta("./imagenes/sales.png")
icon = tk.PhotoImage(file=rutaIcono)#No se redimensiona
root.iconphoto(False,icon)
#Geometry
centrar_ventana(root,1024,600)

barra_superior = tk.Frame(root,height=50
                          ,bg=COLOR_BARRA_SUPERIOR)
barra_superior.pack(side=tk.TOP, fill="both")

menu_lateral = tk.Frame(root,width=150,bg=COLOR_MENU_LATERAL)
menu_lateral.pack(side=tk.LEFT,fill="both",expand=False)

panel_principal = tk.Frame(root,width=150
                           ,bg=COLOR_PANEL_PRINCIPAL)
panel_principal.pack(side=tk.RIGHT ,fill="both",expand=True)


#fuentes_disponibles = list(font.families())
#fa_fonts = [f for f in fuentes_disponibles if "Awesome" in f]
#print(fa_fonts)
fontawesome = font.Font(family="Font Awesome 7 Free",size=18)

btn_menu= tk.Button(barra_superior, text="\uf0c9",
            font=fontawesome,
            bg=COLOR_BARRA_SUPERIOR,
            fg="#f2f2f2",
            bd=0, command=toggle_panel
)

btn_menu.pack(padx=10,pady=10,side=tk.LEFT)

label = tk.Label(barra_superior,text="Programacion I"
                 ,font="Roboto 24"
                 , bg=COLOR_BARRA_SUPERIOR
                 , fg="#f2f2f2"
                 )
label.pack(padx=10,pady=10,side=tk.LEFT)

label_musica = tk.Label(barra_superior
                        ,text=nombre_archivo
                        ,font="Roboto 16", bg=COLOR_BARRA_SUPERIOR
                        ,fg="#f2f2f2"
)



btn_open= tk.Button(barra_superior, text="\uf07c",
            font=fontawesome,
            bg=COLOR_BARRA_SUPERIOR,
            fg="#f2f2f2",
            bd=0, command=cargar_cancion
)

btn_stop= tk.Button(barra_superior, text="\uf04d",
            font=fontawesome,
            bg=COLOR_BARRA_SUPERIOR,
            fg="#f2f2f2",
            bd=0, command=detener
)


btn_play= tk.Button(barra_superior, text="\uf04b",
            font=fontawesome,
            bg=COLOR_BARRA_SUPERIOR,
            fg="#f2f2f2",
            bd=0, command=reproducir
)

btn_pause= tk.Button(barra_superior, text="\uf04c",
            font=fontawesome,
            bg=COLOR_BARRA_SUPERIOR,
            fg="#f2f2f2",
            bd=0, command=pausar
)

volumen = tk.Scale(barra_superior, from_=0, to=100
                   , bg=COLOR_BARRA_SUPERIOR
                   ,fg="#f2f2f2", bd=0,border=0
                   , resolution=1,orient="horizontal"
                   , length=200, troughcolor="#95a5a6"
                   ,activebackground="#0099CC"
                   ,sliderrelief="flat",relief="flat"
                   ,highlightthickness=0
                   )
volumen.set(50)
volumen.pack(padx=4,pady=10, side=tk.RIGHT)
btn_pause.pack(padx=4,pady=10,side=tk.RIGHT)
btn_play.pack(padx=4,pady=10,side=tk.RIGHT)
btn_stop.pack(padx=4,pady=10,side=tk.RIGHT)
btn_open.pack(padx=4,pady=10,side=tk.RIGHT)
label_musica.pack(padx=4,pady=10,side=tk.RIGHT)

ruta_perfil = resolver_ruta("./imagenes/profile.png")
imagen_perfil = leer_imagen(ruta_perfil,(100,100))
label_perfil = tk.Label(menu_lateral, bg=COLOR_MENU_LATERAL
                        ,image=imagen_perfil)
label_perfil.pack(side=tk.TOP,pady=20)

btn_inicio = tk.Button(
    menu_lateral, text="\uf015 Inicio",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=12, font=fontawesome, anchor="w"
    ,command=mostrar_inicio
)

btn_inicio.pack(side=tk.TOP)

btn_ventas = tk.Button(
    menu_lateral, text="\uf4c0 Ventas",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=12, font=fontawesome, anchor="w"
    ,command=mostrar_ventas
)

btn_ventas.pack(side=tk.TOP)
btn_productos = tk.Button(
    menu_lateral, text="\uf468 Productos",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=12, font=fontawesome, anchor="w"
)

btn_productos.pack(side=tk.TOP)
btn_reportes = tk.Button(
    menu_lateral, text="\uf201 Reportes",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=12, font=fontawesome, anchor="w"
)

btn_reportes.pack(side=tk.TOP)
btn_usuarios = tk.Button(
    menu_lateral, text="\uf007 Usuarios",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=12, font=fontawesome, anchor="w"
)

btn_usuarios.pack(side=tk.TOP)
btn_salir = tk.Button(
    menu_lateral, text="\uf2f6 Salir",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=12, font=fontawesome, anchor="w"
    , command=salir
)

btn_salir.pack(side=tk.BOTTOM)

bind_hover_events(btn_inicio)
bind_hover_events(btn_ventas)
bind_hover_events(btn_productos)
bind_hover_events(btn_usuarios)
bind_hover_events(btn_reportes)
bind_hover_events(btn_salir)

root.mainloop()