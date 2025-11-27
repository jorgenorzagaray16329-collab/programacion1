import tkinter as tk
from tkinter import font,filedialog, messagebox
from config import TITULO,COLOR_BARRA_SUPERIOR,COLOR_MENU_LATERAL,COLOR_PANEL_PRINCIPAL
from util.util_ventana import centrar_ventana
from util.util_imagenes import leer_imagen
import pygame
import os

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
    ruta = filedialog.askopenfile(title="Elige un mp3"
                        ,filetypes=[("Archivos MP3","*.mp3")])
    if ruta:
        return (ruta,os.path.basename(ruta))
    
def reproducir(ruta,estado):
    if ruta:
        try:
            if estado=="pause":
                #Si estaba pausado , le quitamos el pause
                pygame.mixer.music.unpause()
                estado="play"
            else:
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
    return "pause"

def detener():
    pygame.mixer.music.stop()
    return "stop"

def cambiar_volumen(valor):
    #El volumnen va de 0 a 1 
    pygame.mixer.music.set_volume(float((valor/100)))

root = tk.Tk()
root.title(TITULO)
icon = tk.PhotoImage(file="./imagenes/sales.png")#No se redimensiona
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
fontawesome = font.Font(family="Font Awesome 7 Free",size=20)

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


btn_stop= tk.Button(barra_superior, text="\uf04d",
            font=fontawesome,
            bg=COLOR_BARRA_SUPERIOR,
            fg="#f2f2f2",
            bd=0
)


btn_play= tk.Button(barra_superior, text="\uf04b",
            font=fontawesome,
            bg=COLOR_BARRA_SUPERIOR,
            fg="#f2f2f2",
            bd=0
)

btn_pause= tk.Button(barra_superior, text="\uf04c",
            font=fontawesome,
            bg=COLOR_BARRA_SUPERIOR,
            fg="#f2f2f2",
            bd=0
)

volumen = tk.Scale(barra_superior, from_=0, to=100
                   , bg=COLOR_BARRA_SUPERIOR
                   ,fg="#f2f2f2", bd=0,border=0
                   , resolution=1,orient="horizontal")
volumen.pack(padx=4,pady=10, side=tk.RIGHT)
btn_pause.pack(padx=4,pady=10,side=tk.RIGHT)
btn_play.pack(padx=4,pady=10,side=tk.RIGHT)
btn_stop.pack(padx=4,pady=10,side=tk.RIGHT)

imagen_perfil = leer_imagen("./imagenes/profile.png",(100,100))
label_perfil = tk.Label(menu_lateral, bg=COLOR_MENU_LATERAL
                        ,image=imagen_perfil)
label_perfil.pack(side=tk.TOP,pady=20)

btn_inicio = tk.Button(
    menu_lateral, text="\uf015 Inicio",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=12, font=fontawesome
    ,command=mostrar_inicio
)

btn_inicio.pack(side=tk.TOP)

btn_ventas = tk.Button(
    menu_lateral, text="\uf4c0 Ventas",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=12, font=fontawesome
    ,command=mostrar_ventas
)

btn_ventas.pack(side=tk.TOP)
btn_productos = tk.Button(
    menu_lateral, text="\uf468 Productos",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=12, font=fontawesome
)

btn_productos.pack(side=tk.TOP)
btn_reportes = tk.Button(
    menu_lateral, text="\uf201 Reportes",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=12, font=fontawesome
)

btn_reportes.pack(side=tk.TOP)
btn_usuarios = tk.Button(
    menu_lateral, text="\uf007 Usuarios",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=12, font=fontawesome
)

btn_usuarios.pack(side=tk.TOP)
btn_salir = tk.Button(
    menu_lateral, text="\uf2f6 Salir",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=12, font=fontawesome
)

btn_salir.pack(side=tk.BOTTOM)

bind_hover_events(btn_inicio)
bind_hover_events(btn_ventas)
bind_hover_events(btn_productos)
bind_hover_events(btn_usuarios)
bind_hover_events(btn_reportes)
bind_hover_events(btn_salir)

root.mainloop()