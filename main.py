# main.py — Life Simulator v0.4.1 (carga por número arreglada)

from utils import (
    limpiar_pantalla, caja, separador, BOLD, CYAN, BLANCO,
    AMARILLO, VERDE, ROJO, RESET,
    guardar_partida, listar_partidas, cargar_partida
)
from talentos import TALENTOS_DISPONIBLES, mostrar_talentos
from eventos import obtener_evento, aplicar_efectos
from logros import verificar_logros, mostrar_logros


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
    if datos_guardados:
        edad = datos_guardados["edad"]
        atributos = datos_guardados["atributos"]
        genero = datos_guardados["genero"]
        talentos = datos_guardados["talentos"]
        historia = datos_guardados["historia"]
        nombre_partida = datos_guardados["nombre"]
        limpiar_pantalla()
        print(f"\n{VERDE}📂 Partida '{nombre_partida}' cargada.{RESET}")
        print(f"{BLANCO}Año actual: {edad}  |  Estado: {'💀 Muerto' if datos_guardados.get('muerto') else '🟢 Vivo'}{RESET}")
        print(f"\n{BOLD}Últimos eventos:{RESET}")
        for linea in historia[-3:]:
            print(f"   {linea}")
        input(f"\n{CYAN}Presiona Enter para continuar...{RESET}")
    else:
        limpiar_pantalla()
        caja("SIMULADOR DE VIDA", "v0.4.1 — Rareza de eventos y sistema de logros")
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
        nacimiento = f"[{edad} años: Naciste, un {genero}"
        if atributos["antecedentes"] >= 10:
            nacimiento += ", rico de segunda generación]"
        elif atributos["antecedentes"] >= 5:
            nacimiento += ", en una familia adinerada]"
        else:
            nacimiento += ", en una familia humilde]"
        print(f"{BLANCO}{nacimiento}{RESET}")
        historia.append(nacimiento)
        print(f"\n{AMARILLO}¿Nombre para guardar esta partida?{RESET}")
        nombre_partida = input("> ").strip()
        if not nombre_partida:
            nombre_partida = f"Partida_{genero}_{atributos['apariencia']}"
    while True:
        if datos_guardados and datos_guardados.get("muerto"):
            print(f"\n{ROJO}Esta partida ya terminó. No se puede continuar.{RESET}")
            input("Enter para volver...")
            return
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
        edad += 1
        evento = obtener_evento(edad, atributos, genero, talentos)
        texto_evento = f"[{edad} años: {evento['texto']}]"
        rareza = evento.get("rareza", "comun")
        color_rareza = {"comun": BLANCO, "raro": CYAN, "epico": AMARILLO, "legendario": ROJO}
        simbolo = {"comun": "", "raro": "⭐ ", "epico": "✨ ", "legendario": "👑 "}
        print(f"\n{color_rareza[rareza]}{simbolo[rareza]}{texto_evento}{RESET}")
        historia.append(texto_evento)
        vivo = aplicar_efectos(atributos, evento["efectos"])
        mostrar_estado(edad, atributos)
        datos_finales = {
            "nombre": nombre_partida,
            "edad": edad,
            "atributos": atributos,
            "genero": genero,
            "talentos": talentos,
            "historia": historia,
            "muerto": not vivo
        }
        if not vivo:
            print(f"\n{ROJO}{BOLD}💀 HAS MUERTO A LOS {edad} AÑOS.{RESET}")
            historia.append(f"[{edad} años: Fallecimiento]")
            break
        if edad >= 100:
            print(f"\n{VERDE}{BOLD}🎉 100 AÑOS. ERES LEGENDARIO.{RESET}")
            break
    nuevos_logros = verificar_logros(datos_finales)
    if nuevos_logros:
        print(f"\n{BOLD}{VERDE}🏆 NUEVOS LOGROS DESBLOQUEADOS:{RESET}")
        for logro in nuevos_logros:
            print(f"   {AMARILLO}⭐ {logro['nombre']}{RESET} — {logro['descripcion']}")
    else:
        print(f"\n{BLANCO}Ningún logro nuevo esta vez.{RESET}")
    guardar_partida(nombre_partida, datos_finales)
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
        caja("LIFE SIMULATOR", "v0.4.1 — Hecho con Python en Pydroid 3")
        print(f"\n{BOLD}{AMARILLO}🎮 MENÚ PRINCIPAL{RESET}\n")
        print("  1. 🆕 Nueva partida")
        print("  2. 📂 Cargar partida")
        print("  3. 🏆 Ver logros")
        print("  4. 🚪 Salir")
        opcion = input(f"\n{CYAN}Elige: {RESET}")
        if opcion == "1":
            jugar_partida()
        elif opcion == "2":
            nombres = listar_partidas()
            if nombres:
                print(f"\n{AMARILLO}Escribe el número de la partida:{RESET}")
                try:
                    num = int(input("> "))
                    if 1 <= num <= len(nombres):
                        nombre = nombres[num - 1]
                        datos = cargar_partida(nombre)
                        if datos:
                            jugar_partida(datos)
                        else:
                            print(f"{ROJO}Error al cargar.{RESET}")
                            input("Enter para continuar...")
                    else:
                        print(f"{ROJO}Número fuera de rango.{RESET}")
                        input("Enter para continuar...")
                except ValueError:
                    print(f"{ROJO}Escribe un número.{RESET}")
                    input("Enter para continuar...")
        elif opcion == "3":
            mostrar_logros()
            input("\nPresiona Enter para volver...")
        elif opcion == "4":
            print(f"\n{VERDE}👋 Gracias por jugar.{RESET}")
            break
        else:
            print(f"{ROJO}Opción no válida.{RESET}")
            input("Enter para continuar...")


if __name__ == "__main__":
    menu_principal()
