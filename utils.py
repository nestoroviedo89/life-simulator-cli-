# utils.py
# Life Simulator v0.6.0
# Utilidades, colores y sistema de guardado


import json
import os


# =========================
# COLORES
# =========================

RESET = "\033[0m"
BOLD = "\033[1m"

ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
CYAN = "\033[96m"
BLANCO = "\033[97m"


# =========================
# ARCHIVO DE PARTIDAS
# =========================

ARCHIVO_PARTIDAS = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    ),
    "life_sim_partidas.json"
)


# =========================
# LIMPIAR PANTALLA
# =========================

def limpiar_pantalla():

    os.system(
        "cls"
        if os.name == "nt"
        else "clear"
    )


# =========================
# CAJA DE TEXTO
# =========================

def caja(titulo, subtitulo=""):

    print(
        "\n" + "=" * 50
    )

    print(
        titulo.center(50)
    )

    print(
        "=" * 50
    )

    if subtitulo:

        print(
            subtitulo.center(50)
        )

    print(
        "=" * 50
    )


# =========================
# CARGAR TODAS LAS PARTIDAS
# =========================

def cargar_partidas():

    if not os.path.exists(
        ARCHIVO_PARTIDAS
    ):

        return {}

    try:

        with open(
            ARCHIVO_PARTIDAS,
            "r",
            encoding="utf-8"
        ) as archivo:

            datos = json.load(
                archivo
            )

            if isinstance(
                datos,
                dict
            ):

                return datos

            return {}

    except (
        json.JSONDecodeError,
        OSError
    ):

        return {}


# =========================
# GUARDAR TODAS LAS PARTIDAS
# =========================

def guardar_partidas(
    partidas
):

    with open(
        ARCHIVO_PARTIDAS,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            partidas,
            archivo,
            ensure_ascii=False,
            indent=4
        )


# =========================
# GUARDAR PARTIDA
# =========================

def guardar_partida(
    nombre,
    personaje,
    alma
):

    partidas = cargar_partidas()

    partidas[nombre] = {
        "personaje":
            personaje.convertir_a_dict(
                nombre
            ),

        "alma":
            alma.convertir_a_dict()
    }

    guardar_partidas(
        partidas
    )

    return True


# =========================
# LISTAR PARTIDAS
# =========================

def listar_partidas():

    partidas = cargar_partidas()

    if not partidas:

        return []

    return list(
        partidas.keys()
    )


# =========================
# CARGAR PARTIDA
# =========================

def cargar_partida(
    nombre
):

    partidas = cargar_partidas()

    return partidas.get(
        nombre
    )


# =========================
# ELIMINAR PARTIDA
# =========================

def eliminar_partida(
    nombre
):

    partidas = cargar_partidas()

    if nombre not in partidas:

        return False

    del partidas[nombre]

    guardar_partidas(
        partidas
    )

    return True