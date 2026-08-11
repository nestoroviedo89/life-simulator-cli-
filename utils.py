# utils.py — Colores, utilidades y guardado de partidas

import json
import os

# === COLORES ANSI ===
NEGRO = "\033[40m"
AZUL = "\033[44m"
CYAN = "\033[46m"
BLANCO = "\033[97m"
AMARILLO = "\033[93m"
VERDE = "\033[92m"
ROJO = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"


def limpiar_pantalla():
    print("\n" * 50)


def caja(titulo, contenido, ancho=50):
    linea = "═" * ancho
    print(f"\n{BOLD}{CYAN}╔{linea}╗{RESET}")
    print(f"{BOLD}{CYAN}║{RESET}{BLANCO}{titulo:^{ancho}}{RESET}{BOLD}{CYAN}║{RESET}")
    print(f"{BOLD}{CYAN}╠{linea}╣{RESET}")
    for linea_texto in contenido.split("\n"):
        print(f"{BOLD}{CYAN}║{RESET} {linea_texto:<{ancho-2}} {BOLD}{CYAN}║{RESET}")
    print(f"{BOLD}{CYAN}╚{linea}╝{RESET}\n")


def separador():
    print(f"{BOLD}{CYAN}{'─' * 52}{RESET}")


# === GUARDADO DE PARTIDAS ===

ARCHIVO_PARTIDAS = "/storage/emulated/0/Download/life_sim_partidas.json"


def guardar_partida(nombre, datos):
    partidas = cargar_todas_partidas()
    partidas[nombre] = datos
    with open(ARCHIVO_PARTIDAS, "w", encoding="utf-8") as f:
        json.dump(partidas, f, indent=4, ensure_ascii=False)
    print(f"\n{VERDE}💾 Partida '{nombre}' guardada.{RESET}")


def cargar_todas_partidas():
    if not os.path.exists(ARCHIVO_PARTIDAS):
        return {}
    with open(ARCHIVO_PARTIDAS, "r", encoding="utf-8") as f:
        return json.load(f)


def listar_partidas():
    partidas = cargar_todas_partidas()
    if not partidas:
        print(f"\n{AMARILLO}No hay partidas guardadas.{RESET}")
        return None
    print(f"\n{BOLD}{AMARILLO}📁 PARTIDAS GUARDADAS:{RESET}")
    for i, nombre in enumerate(partidas.keys(), 1):
        p = partidas[nombre]
        estado = "💀 Muerto" if p.get("muerto") else "🟢 Vivo"
        print(f"  {CYAN}[{i}]{RESET} {nombre} — {estado} a los {p['edad']} años")
    print(f"\n{BLANCO}Escribe el número para cargar.{RESET}")
    return list(partidas.keys())


def cargar_partida(nombre):
    partidas = cargar_todas_partidas()
    return partidas.get(nombre)
    
