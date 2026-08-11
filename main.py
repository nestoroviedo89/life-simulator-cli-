# main.py — Life Simulator v0.3 (con guardado y menú)

import time
from utils import (
    limpiar_pantalla, caja, separador, BOLD, CYAN, BLANCO, 
    AMARILLO, VERDE, ROJO, RESET,
    guardar_partida, listar_partidas, cargar_partida
)
from talentos import TALENTOS_DISPONIBLES, mostrar_talentos
from eventos import obtener_evento, aplicar_efectos


def seleccionar_talentos():
    mostrar_talentos()
    seleccionados = []
    print(f"{AMARILLO}Elige 3 talentos (números separados por espacio):{RESET}")
    entrada = input("> ")
    
    try:
        ids = [int(x) for x in entrada.split()]
        if len(ids) != 3:
            print(f"{ROJO}Debes elegir exactamente 3.{RESET}")
            return seleccionar_talentos()
        for tid in ids:
            talento = next((t for t in TALENTOS_DISPONIBLES if t["id"] == tid), None)
            if talento is None:
                print(f"{ROJO}ID {tid} inválido.{RESET}")
                return seleccionar_talentos()
            seleccionados.append(talento)
    except ValueError:
        print(f"{ROJO}Solo números separados por espacio.{RESET}")
        return seleccionar_talentos()
    
    return seleccionados


def aplicar_talentos(talentos):
    base = {"apariencia": 0, "inteligencia": 0, "fisico": 0, "antecedentes": 0}
    for t in talentos:
        for key in base:
            base[key] += t["efectos"][key]
    return base


def asignar_atributos(atributos):
    puntos = 20
    print(f"\n{BOLD}{AMARILLO}📊 DISTRIBUYE {puntos} PUNTOS{RESET}")
    for attr in ["apariencia", "inteligencia", "fisico", "antecedentes"]:
        while True:
            try:
                msg = f"{attr.capitalize()} (restantes: {puntos}): "
                pts = int(input(msg))
                if pts < 0 or pts > puntos:
                    print(f"Máximo {puntos}, mínimo 0.")
                    continue
                atributos[attr] += pts
                puntos -= pts
                break
            except ValueError:
                print("Escribe un número.")
    return atributos


def determinar_genero():
    import random
    return random.choice(["niño", "niña"])


def mostrar_estado(edad, atributos):
    print(f"\n{BOLD}{CYAN}📅 Año {edad}{RESET}")
    print(f"   Apariencia: {atributos['apariencia']}  |  Inteligencia: {atributos['inteligencia']}")
    print(f"   Físico: {atributos['fisico']}  |  Antecedentes: {atributos['antecedentes']}")
    print()


def jugar_partida(datos_guardados=None):
    """Loop principal del juego. Puede recibir datos guardados."""
    
    if datos_guardados:
        # Cargar partida existente
        edad = datos_guardados["edad"]
        atributos = datos_guardados["atributos"]
        genero = datos_guardados["genero"]
        talentos = datos_guardados["talentos"]
        historia = datos_guardados["historia"]
        nombre_partida = datos_guardados["nombre"]
        print(f"\n{VERDE}📂 Partida '{nombre_partida}' cargada. Año {edad}.{RESET}")
    else:
        # Nueva partida
        limpiar_pantalla()
        caja("SIMULADOR DE VIDA", "Crea tu personaje y observa su destino")
        
        talentos = seleccionar_talentos()
        atributos = aplicar_talentos(talentos)
        atributos = asignar_atributos(atributos)
        genero = determinar_genero()
        
        limpiar_pantalla()
        caja("TU PERSONAJE", f"Género: {genero.capitalize()}\nApariencia: {atributos['apariencia']}\nInteligencia: {atributos['inteligencia']}\nFísico: {atributos['fisico']}\nAntecedentes: {atributos['antecedentes']}")
        
        print(f"\n{BOLD}{CYAN}📖 TU HISTORIA COMIENZA...{RESET}\n")
        input("Presiona Enter para empezar...")
        
        edad = 0
        historia = []
        
        # Nacimiento
        nacimiento = f"[{edad} años: Naciste, un {genero}"
        if atributos["antecedentes"] >= 10:
            nacimiento += ", rico de segunda generación]"
        elif atributos["antecedentes"] >= 5:
            nacimiento += ", en una familia adinerada]"
        else:
            nacimiento += ", en una familia humilde]"
        
        print(f"{BLANCO}{nacimiento}{RESET}")
        historia.append(nacimiento)
        
        # Pedir nombre para guardar
        print(f"\n{AMARILLO}¿Nombre para guardar esta partida?{RESET}")
        nombre_partida = input("> ").strip()
        if not nombre_partida:
            nombre_partida = f"Partida_{genero}_{atributos['apariencia']}"
    
    # --- LOOP DE VIDA ---
    while True:
        print(f"\n{CYAN}1. Avanzar un año  |  2. Guardar y salir{RESET}")
        opcion = input("> ")
        
        if opcion == "2":
            datos = {
                "nombre": nombre_partida,
                "edad": edad,
                "atributos": atributos,
                "genero": genero,
                "talentos": talentos,
                "historia": historia,
                "muerto": False
            }
            guardar_partida(nombre_partida, datos)
            return
        
        # Avanzar año
        edad += 1
        evento = obtener_evento(edad, atributos, genero, talentos)
        texto_evento = f"[{edad} años: {evento['texto']}]"
        
        print(f"\n{AMARILLO}{texto_evento}{RESET}")
        historia.append(texto_evento)
        
        vivo = aplicar_efectos(atributos, evento["efectos"])
        mostrar_estado(edad, atributos)
        
        if not vivo:
            print(f"\n{ROJO}{BOLD}💀 HAS MUERTO A LOS {edad} AÑOS.{RESET}")
            historia.append(f"[{edad} años: Fallecimiento]")
            
            # Guardar como partida terminada
            datos = {
                "nombre": nombre_partida,
                "edad": edad,
                "atributos": atributos,
                "genero": genero,
                "talentos": talentos,
                "historia": historia,
                "muerto": True
            }
            guardar_partida(nombre_partida, datos)
            break
        
        if edad >= 100:
            print(f"\n{VERDE}{BOLD}🎉 100 AÑOS. ERES LEGENDARIO.{RESET}")
            datos = {
                "nombre": nombre_partida,
                "edad": edad,
                "atributos": atributos,
                "genero": genero,
                "talentos": talentos,
                "historia": historia,
                "muerto": False
            }
            guardar_partida(nombre_partida, datos)
            break
    
    # --- RESUMEN ---
    separador()
    print(f"\n{BOLD}{CYAN}📜 RESUMEN DE TU VIDA ({edad} años){RESET}\n")
    for linea in historia:
        print(f"   {linea}")
    
    print(f"\n{BOLD}Atributos finales:{RESET}")
    for k, v in atributos.items():
        print(f"   {k.capitalize()}: {v}")
    
    input(f"\n{CYAN}Presiona Enter para volver al menú...{RESET}")


def menu_principal():
    while True:
        limpiar_pantalla()
        caja("LIFE SIMULATOR", "v0.3 — Hecho con Python en Pydroid 3")
        
        print(f"\n{BOLD}{AMARILLO}🎮 MENÚ PRINCIPAL{RESET}\n")
        print("  1. 🆕 Nueva partida")
        print("  2. 📂 Cargar partida")
        print("  3. 📊 Ver estadísticas")
        print("  4. 🚪 Salir")
        
        opcion = input(f"\n{CYAN}Elige: {RESET}")
        
        if opcion == "1":
            jugar_partida()
        elif opcion == "2":
            nombres = listar_partidas()
            if nombres:
                print(f"\n{AMARILLO}Escribe el nombre exacto de la partida:{RESET}")
                nombre = input("> ")
                datos = cargar_partida(nombre)
                if datos:
                    jugar_partida(datos)
                else:
                    print(f"{ROJO}Partida no encontrada.{RESET}")
                    input("Enter para continuar...")
        elif opcion == "3":
            listar_partidas()
            input("\nPresiona Enter para volver...")
        elif opcion == "4":
            print(f"\n{VERDE}👋 Gracias por jugar.{RESET}")
            break
        else:
            print(f"{ROJO}Opción no válida.{RESET}")
            input("Enter para continuar...")


if __name__ == "__main__":
    menu_principal()
