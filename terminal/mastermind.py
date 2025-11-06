from colorama import init,Fore,Style
import random

# configuracion del juego
COLORES_POSIBLES = {
    "N": Fore.BLACK+"▮",
    "R": Fore.RED+"▮",
    "V": Fore.GREEN+"▮",
    "Y": Fore.YELLOW+"▮",
    "A": Fore.BLUE+"▮",
    "M": Fore.MAGENTA+"▮",
    "C": Fore.CYAN+"▮",
    "B": Fore.WHITE+"▮"
}

LONGITUD_CODIGO = 4
MAX_INTENTOS = 8

def generar_codigo():
    colores = list(COLORES_POSIBLES.keys())
    codigo_secreto = []
    for _ in range(LONGITUD_CODIGO):
        codigo_secreto.append(random.choice(colores))
    return codigo_secreto


def mostrar_colores_disponibles():
    print("Colores disponibles:")
    for letra,color_formato in COLORES_POSIBLES.items():
        print(f" {letra}: {color_formato} {Style.RESET_ALL}", end=" ")


def obtener_intento_usuario():
    while True:
        intento = input(f"Ingresa tu código de {LONGITUD_CODIGO} letras:\n").upper().strip()

        if len(intento) != LONGITUD_CODIGO:
            print(Fore.RED+f"Error: El código debe tener {LONGITUD_CODIGO} letras"+Style.RESET_ALL)
            continue

        valido = True
        for letra in intento:
            if letra not in COLORES_POSIBLES:
                print(Fore.RED+f"Error: La letra '{letra}' no es un color valido. "+Style.RESET_ALL)
                valido = False
                break

        if valido:
            return list(intento)


def evaluar_intento(intento,codigo_secreto):
    #Evalua el intento y devuelve las pistas 
    return #posicion correcta, color correcto
        