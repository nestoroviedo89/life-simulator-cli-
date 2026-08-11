# logros.py — Sistema de logros persistentes

import os
import json
from utils import VERDE, AMARILLO, RESET, BOLD

ARCHIVO_LOGROS = "/storage/emulated/0/Download/life_sim_logros.json"


# Definición de todos los logros posibles
# Cada uno tiene una función condición que recibe los datos de la partida
LOGROS_DEFINICION = [
    {
        "id": "primer_muerte",
        "nombre": "Iniciado",
        "descripcion": "Muere por primera vez",
        "condicion": lambda d: d.get("muerto") is True
    },
    {
        "id": "sobreviviente_prematuro",
        "nombre": "Milagro",
        "descripcion": "Sobrevive siendo Bebé prematuro hasta los 10 años",
        "condicion": lambda d: any(t["nombre"] == "Bebé prematuro" for t in d["talentos"]) and d["edad"] >= 10
    },
    {
        "id": "centenario",
        "nombre": "Inmortal",
        "descripcion": "Llega a los 100 años",
        "condicion": lambda d: d["edad"] >= 100
    },
    {
        "id": "rico",
        "nombre": "Magnate",
        "descripcion": "Alcanza 30 o más en Antecedentes",
        "condicion": lambda d: d["atributos"]["antecedentes"] >= 30
    },
    {
        "id": "genio",
        "nombre": "Einstein",
        "descripcion": "Alcanza 25 o más en Inteligencia",
        "condicion": lambda d: d["atributos"]["inteligencia"] >= 25
    },
    {
        "id": "hermoso",
        "nombre": "Divino",
        "descripcion": "Alcanza 25 o más en Apariencia",
        "condicion": lambda d: d["atributos"]["apariencia"] >= 25
    },
    {
        "id": "atleta",
        "nombre": "Hércules",
        "descripcion": "Alcanza 25 o más en Físico",
        "condicion": lambda d: d["atributos"]["fisico"] >= 25
    },
    {
        "id": "skyfall",
        "nombre": "Elegido",
        "descripcion": "Juega con el talento Sistema Skyfall",
        "condicion": lambda d: any(t["nombre"] == "Sistema Skyfall" for t in d["talentos"])
    },
    {
        "id": "muerte_temprana",
        "nombre": "Vela corta",
        "descripcion": "Muere antes de los 5 años",
        "condicion": lambda d: d.get("muerto") is True and d["edad"] < 5
    },
    {
        "id": "vida_media",
        "nombre": "Promedio",
        "descripcion": "Vive entre 50 y 70 años",
        "condicion": lambda d: d.get("muerto") is True and 50 <= d["edad"] <= 70
    },
]


def cargar_logros():
    if not os.path.exists(ARCHIVO_LOGROS):
        return set()
    with open(ARCHIVO_LOGROS, "r", encoding="utf-8") as f:
        return set(json.load(f))


def guardar_logros(logros):
    with open(ARCHIVO_LOGROS, "w", encoding="utf-8") as f:
        json.dump(list(logros), f, indent=4, ensure_ascii=False)


def verificar_logros(datos_partida):
    """Recibe los datos de la partida y devuelve los nuevos logros desbloqueados."""
    logros_actuales = cargar_logros()
    nuevos = []
    
    for logro in LOGROS_DEFINICION:
        if logro["id"] not in logros_actuales:
            if logro["condicion"](datos_partida):
                logros_actuales.add(logro["id"])
                nuevos.append(logro)
    
    if nuevos:
        guardar_logros(logros_actuales)
    
    return nuevos


def mostrar_logros():
    """Muestra todos los logros con estado desbloqueado o bloqueado."""
    desbloqueados = cargar_logros()
    total = len(LOGROS_DEFINICION)
    
    print(f"\n{BOLD}{AMARILLO}🏆 LOGROS ({len(desbloqueados)}/{total}){RESET}\n")
    
    for logro in LOGROS_DEFINICION:
        if logro["id"] in desbloqueados:
            print(f"  {VERDE}✅{RESET} {BOLD}{logro['nombre']}{RESET}")
            print(f"      {logro['descripcion']}")
        else:
            print(f"  ⬜ ???")
            print(f"      {logro['descripcion']}")
        print()
