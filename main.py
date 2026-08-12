# main.py
# Life Simulator v0.6.0
# Personaje + Eventos + Logros + Alma + Reencarnación
# Guardado y carga de personaje + alma


from utils import (
    limpiar_pantalla,
    caja,
    BOLD,
    CYAN,
    BLANCO,
    AMARILLO,
    VERDE,
    ROJO,
    RESET,
    guardar_partida,
    listar_partidas,
    cargar_partida
)

from talentos import (
    TALENTOS_DISPONIBLES,
    mostrar_talentos
)

from eventos import (
    obtener_evento,
    aplicar_efectos
)

from logros import (
    verificar_logros,
    mostrar_logros
)

from personaje import Personaje

from alma import Alma


# =========================
# CREACIÓN DEL PERSONAJE
# =========================

def determinar_genero():

    import random

    return random.choice([
        "niño",
        "niña"
    ])


def seleccionar_talentos():

    mostrar_talentos()

    while True:

        print(
            f"{AMARILLO}"
            "Elige 3 talentos "
            "(números separados por espacio):"
            f"{RESET}"
        )

        entrada = input("> ")

        try:

            ids = [
                int(x)
                for x in entrada.split()
            ]

            if len(ids) != 3:

                print(
                    f"{ROJO}"
                    "Debes elegir exactamente 3."
                    f"{RESET}"
                )

                continue

            seleccionados = []

            valido = True

            for tid in ids:

                talento = next(
                    (
                        t
                        for t in TALENTOS_DISPONIBLES
                        if t["id"] == tid
                    ),
                    None
                )

                if talento is None:

                    print(
                        f"{ROJO}"
                        f"ID {tid} inválido."
                        f"{RESET}"
                    )

                    valido = False

                    break

                seleccionados.append(
                    talento
                )

            if valido:

                return seleccionados

        except ValueError:

            print(
                f"{ROJO}"
                "Solo números separados por espacio."
                f"{RESET}"
            )


def aplicar_talentos(talentos):

    atributos = {
        "apariencia": 0,
        "inteligencia": 0,
        "fisico": 0,
        "antecedentes": 0
    }

    for talento in talentos:

        for atributo in atributos:

            atributos[atributo] += (
                talento["efectos"][atributo]
            )

    return atributos


def asignar_atributos(atributos):

    puntos = 20

    print(
        f"\n{BOLD}{AMARILLO}"
        f"📊 DISTRIBUYE {puntos} PUNTOS"
        f"{RESET}"
    )

    for atributo in [
        "apariencia",
        "inteligencia",
        "fisico",
        "antecedentes"
    ]:

        while True:

            try:

                cantidad = int(
                    input(
                        f"{atributo.capitalize()} "
                        f"(restantes: {puntos}): "
                    )
                )

                if cantidad < 0 or cantidad > puntos:

                    print(
                        f"{ROJO}"
                        f"Debes elegir entre 0 y {puntos}."
                        f"{RESET}"
                    )

                    continue

                atributos[atributo] += (
                    cantidad
                )

                puntos -= cantidad

                break

            except ValueError:

                print(
                    f"{ROJO}"
                    "Escribe un número."
                    f"{RESET}"
                )

    return atributos


# =========================
# CREAR PERSONAJE
# =========================

def crear_personaje(alma):

    talentos = seleccionar_talentos()

    atributos = aplicar_talentos(
        talentos
    )

    atributos = asignar_atributos(
        atributos
    )

    genero = determinar_genero()

    historia = []

    personaje = Personaje(
        edad=0,
        genero=genero,
        atributos=atributos,
        talentos=talentos,
        historia=historia
    )

    # Aplicar herencia del alma
    personaje.aplicar_herencia(
        alma.obtener_herencia()
    )

    return personaje


# =========================
# EVENTOS
# =========================

def mostrar_evento(evento, edad):

    texto = evento["texto"]

    rareza = evento.get(
        "rareza",
        "comun"
    )

    colores = {
        "comun": BLANCO,
        "raro": CYAN,
        "epico": AMARILLO,
        "legendario": ROJO
    }

    simbolos = {
        "comun": "",
        "raro": "⭐ ",
        "epico": "✨ ",
        "legendario": "👑 "
    }

    color = colores.get(
        rareza,
        BLANCO
    )

    simbolo = simbolos.get(
        rareza,
        ""
    )

    texto_completo = (
        f"[{edad} años: {texto}]"
    )

    print(
        f"\n{color}"
        f"{simbolo}"
        f"{texto_completo}"
        f"{RESET}"
    )

    return texto_completo


def comprobar_logros(
    personaje,
    evento
):

    try:

        nuevos = verificar_logros(
            personaje,
            evento
        )

        if nuevos:

            print(
                f"\n{AMARILLO}{BOLD}"
                "🏆 ¡LOGRO DESBLOQUEADO!"
                f"{RESET}"
            )

            for logro in nuevos:

                print(
                    f"{VERDE}"
                    f"🏆 {logro}"
                    f"{RESET}"
                )

    except TypeError:

        pass


def procesar_año(personaje):

    edad = personaje.envejecer()

    evento = obtener_evento(
        edad,
        personaje.atributos,
        personaje.genero,
        personaje.talentos
    )

    texto = mostrar_evento(
        evento,
        edad
    )

    personaje.historia.append(
        texto
    )

    vivo = aplicar_efectos(
        personaje.atributos,
        evento["efectos"]
    )

    comprobar_logros(
        personaje,
        evento
    )

    if not vivo:

        personaje.muerto = True

        muerte = (
            f"[{edad} años: Fallecimiento]"
        )

        personaje.historia.append(
            muerte
        )

        print(
            f"\n{ROJO}{BOLD}"
            f"💀 HAS MUERTO A LOS {edad} AÑOS."
            f"{RESET}"
        )

        return False

    return True


# =========================
# REENCARNACIÓN
# =========================

def reencarnar(
    personaje,
    alma
):

    print(
        f"\n{BOLD}{CYAN}"
        "✨ TU ALMA CONTINÚA"
        f"{RESET}"
    )

    alma.registrar_vida(
        personaje.edad,
        personaje.atributos,
        personaje.talentos
    )

    print(
        f"\n{AMARILLO}"
        f"Vidas completadas: "
        f"{alma.vidas_vividas}"
        f"{RESET}"
    )

    while True:

        print(
            "\n1. 🔄 Reencarnar"
        )

        print(
            "2. 🚪 Terminar partida"
        )

        opcion = input(
            "\nElige: "
        )

        if opcion == "1":

            alma.nueva_vida()

            print(
                f"\n{BOLD}{CYAN}"
                "🔄 REENCARNACIÓN"
                f"{RESET}"
            )

            print(
                "\nTu alma conserva "
                "parte de la experiencia "
                "de tu vida anterior."
            )

            print(
                f"\nVidas vividas: "
                f"{alma.vidas_vividas}"
            )

            print(
                "\n👶 Una nueva vida comienza..."
            )

            input(
                "\nPresiona Enter..."
            )

            return crear_personaje(
                alma
            )

        elif opcion == "2":

            return None

        else:

            print(
                f"{ROJO}"
                "Opción no válida."
                f"{RESET}"
            )


# =========================
# GUARDAR PARTIDA
# =========================

def guardar_partida_actual(
    personaje,
    alma
):

    print(
        f"\n{BOLD}{CYAN}"
        "💾 GUARDAR PARTIDA"
        f"{RESET}"
    )

    nombre = input(
        "Nombre de la partida: "
    ).strip()

    if not nombre:

        print(
            f"{ROJO}"
            "El nombre no puede estar vacío."
            f"{RESET}"
        )

        return

    guardar_partida(
        nombre,
        personaje,
        alma
    )

    print(
        f"\n{VERDE}"
        f"✅ Partida '{nombre}' guardada correctamente."
        f"{RESET}"
    )


# =========================
# CARGAR PARTIDA
# =========================

def cargar_partida_completa():

    partidas = listar_partidas()

    if not partidas:

        print(
            f"\n{AMARILLO}"
            "📂 No hay partidas guardadas."
            f"{RESET}"
        )

        input(
            "\nPresiona Enter..."
        )

        return None

    print(
        f"\n{BOLD}{CYAN}"
        "📂 PARTIDAS GUARDADAS"
        f"{RESET}\n"
    )

    for i, nombre in enumerate(
        partidas,
        start=1
    ):

        print(
            f"{i}. {nombre}"
        )

    print(
        f"{len(partidas) + 1}. Cancelar"
    )

    while True:

        opcion = input(
            "\nElige una partida: "
        )

        try:

            numero = int(opcion)

            if numero == len(partidas) + 1:

                return None

            if 1 <= numero <= len(partidas):

                nombre = partidas[
                    numero - 1
                ]

                datos = cargar_partida(
                    nombre
                )

                if datos is None:

                    print(
                        f"{ROJO}"
                        "No se pudo cargar la partida."
                        f"{RESET}"
                    )

                    return None

                # =========================
                # COMPATIBILIDAD
                # =========================

                # Partidas nuevas:
                # personaje + alma

                if (
                    "personaje" in datos
                    and "alma" in datos
                ):

                    personaje = (
                        Personaje.desde_dict(
                            datos["personaje"]
                        )
                    )

                    alma = (
                        Alma.desde_dict(
                            datos["alma"]
                        )
                    )

                # Partidas antiguas:
                # solamente personaje
                else:

                    personaje = (
                        Personaje.desde_dict(
                            datos
                        )
                    )

                    alma = Alma()

                print(
                    f"\n{VERDE}"
                    f"✅ Partida '{nombre}' cargada."
                    f"{RESET}"
                )

                print(
                    f"\n{CYAN}"
                    f"✨ Vida actual: "
                    f"{alma.vida_actual}"
                    f"{RESET}"
                )

                print(
                    f"{CYAN}"
                    f"✨ Vidas vividas: "
                    f"{alma.vidas_vividas}"
                    f"{RESET}"
                )

                input(
                    "\nPresiona Enter..."
                )

                return (
                    personaje,
                    alma
                )

            print(
                f"{ROJO}"
                "Número inválido."
                f"{RESET}"
            )

        except ValueError:

            print(
                f"{ROJO}"
                "Escribe un número."
                f"{RESET}"
            )


# =========================
# MENÚ DE VIDA
# =========================

def mostrar_menu_vida(
    personaje,
    alma
):

    while True:

        limpiar_pantalla()

        caja(
            "VIDA",
            (
                f"Vida #{alma.vida_actual} "
                f"| Edad: {personaje.edad}"
            )
        )

        print(
            f"\n{BOLD}{AMARILLO}"
            "¿Qué deseas hacer?"
            f"{RESET}\n"
        )

        print("1. Avanzar un año")
        print("2. Ver personaje")
        print("3. Ver historia")
        print("4. Ver logros")
        print("5. ✨ Ver alma")
        print("6. 💾 Guardar partida")
        print("7. Salir")

        opcion = input(
            f"\n{CYAN}> {RESET}"
        )

        if opcion == "1":

            vivo = procesar_año(
                personaje
            )

            personaje.mostrar_estado()

            if not vivo:

                input(
                    f"\n{CYAN}"
                    "Presiona Enter..."
                    f"{RESET}"
                )

                nuevo_personaje = reencarnar(
                    personaje,
                    alma
                )

                if nuevo_personaje is None:

                    return False

                personaje = nuevo_personaje

            else:

                input(
                    f"\n{CYAN}"
                    "Presiona Enter para continuar..."
                    f"{RESET}"
                )

        elif opcion == "2":

            personaje.mostrar_estado()

            input(
                f"\n{CYAN}"
                "Presiona Enter..."
                f"{RESET}"
            )

        elif opcion == "3":

            print(
                f"\n{BOLD}{CYAN}"
                "📖 HISTORIA"
                f"{RESET}\n"
            )

            if personaje.historia:

                for evento in (
                    personaje.historia
                ):

                    print(evento)

            else:

                print(
                    "Todavía no hay historia."
                )

            input(
                f"\n{CYAN}"
                "Presiona Enter..."
                f"{RESET}"
            )

        elif opcion == "4":

            try:

                mostrar_logros()

            except TypeError:

                print(
                    "\n🏆 Logros disponibles."
                )

            input(
                f"\n{CYAN}"
                "Presiona Enter..."
                f"{RESET}"
            )

        elif opcion == "5":

            alma.mostrar()

            input(
                f"\n{CYAN}"
                "Presiona Enter..."
                f"{RESET}"
            )

        elif opcion == "6":

            guardar_partida_actual(
                personaje,
                alma
            )

            input(
                f"\n{CYAN}"
                "Presiona Enter..."
                f"{RESET}"
            )

        elif opcion == "7":

            return True

        else:

            print(
                f"\n{ROJO}"
                "Opción no válida."
                f"{RESET}"
            )

            input(
                "Presiona Enter..."
            )


# =========================
# NUEVA PARTIDA
# =========================

def nueva_partida():

    limpiar_pantalla()

    caja(
        "SIMULADOR DE VIDA",
        "v0.6.0 — Alma y Reencarnación"
    )

    # Una sola alma para todas las vidas
    alma = Alma()

    personaje = crear_personaje(
        alma
    )

    limpiar_pantalla()

    caja(
        "TU HISTORIA COMIENZA",
        (
            f"Vida #{alma.vida_actual} | "
            f"Género: "
            f"{personaje.genero.capitalize()}"
        )
    )

    nacimiento = personaje.nacer()

    print(
        f"\n{BLANCO}"
        f"{nacimiento}"
        f"{RESET}"
    )

    print(
        f"\n{BOLD}{CYAN}"
        "📊 ESTADO INICIAL"
        f"{RESET}"
    )

    personaje.mostrar_estado()

    input(
        f"\n{CYAN}"
        "Presiona Enter para comenzar tu vida..."
        f"{RESET}"
    )

    mostrar_menu_vida(
        personaje,
        alma
    )


# =========================
# MENÚ PRINCIPAL
# =========================

def menu_principal():

    while True:

        limpiar_pantalla()

        caja(
            "LIFE SIMULATOR",
            "v0.6.0 — Alma y Reencarnación"
        )

        print(
            f"\n{BOLD}{AMARILLO}"
            "🎮 MENÚ PRINCIPAL"
            f"{RESET}\n"
        )

        print("1. 🆕 Nueva partida")
        print("2. 📂 Cargar partida")
        print("3. 🏆 Ver logros")
        print("4. 🚪 Salir")

        opcion = input(
            f"\n{CYAN}Elige: {RESET}"
        )

        if opcion == "1":

            nueva_partida()

        elif opcion == "2":

            partida = (
                cargar_partida_completa()
            )

            if partida is not None:

                personaje, alma = partida

                mostrar_menu_vida(
                    personaje,
                    alma
                )

        elif opcion == "3":

            try:

                mostrar_logros()

            except TypeError:

                print(
                    "\n🏆 Logros disponibles."
                )

            input(
                f"\n{CYAN}"
                "Presiona Enter..."
                f"{RESET}"
            )

        elif opcion == "4":

            print(
                f"\n{VERDE}"
                "👋 Gracias por jugar."
                f"{RESET}"
            )

            break

        else:

            print(
                f"\n{ROJO}"
                "Opción no válida."
                f"{RESET}"
            )

            input(
                "Presiona Enter..."
            )


# =========================
# INICIO DEL PROGRAMA
# =========================

if __name__ == "__main__":

    menu_principal()