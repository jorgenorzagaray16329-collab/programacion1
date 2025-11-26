import tkinter as tk
from tkinter import font
from config import TITULO,COLOR_BARRA_SUPERIOR,COLOR_MENU_LATERAL,COLOR_PANEL_PRINCIPAL
from util.util_ventana import centrar_ventana
from util.util_imagenes import leer_imagen

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
            bd=0
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
label_perfil.pack()


root.mainloop()