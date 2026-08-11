# talentos.py — Definición de talentos

TALENTOS_DISPONIBLES = [
    {
        "id": 1,
        "nombre": "Preceptos",
        "descripcion": "Tú, el juego y las drogas son irreconciliables",
        "efectos": {"apariencia": 0, "inteligencia": 2, "fisico": 0, "antecedentes": 0}
    },
    {
        "id": 2,
        "nombre": "Belleza maldita",
        "descripcion": "Valor nominal +3, constitución -2",
        "efectos": {"apariencia": 3, "inteligencia": 0, "fisico": -2, "antecedentes": 0}
    },
    {
        "id": 3,
        "nombre": "Élite antifraude",
        "descripcion": "No te engañarán fácilmente",
        "efectos": {"apariencia": 0, "inteligencia": 3, "fisico": 0, "antecedentes": 1}
    },
    {
        "id": 4,
        "nombre": "Bebé prematuro",
        "descripcion": "Constitución -3, pero más astuto",
        "efectos": {"apariencia": 0, "inteligencia": 2, "fisico": -3, "antecedentes": 0}
    },
    {
        "id": 5,
        "nombre": "Rica segunda generación",
        "descripcion": "Inteligencia +1, físico +2, apariencia +1, antecedentes +5",
        "efectos": {"apariencia": 1, "inteligencia": 1, "fisico": 2, "antecedentes": 5}
    },
    {
        "id": 6,
        "nombre": "Sistema Skyfall",
        "descripcion": "Todos los atributos +10 (legendario)",
        "efectos": {"apariencia": 10, "inteligencia": 10, "fisico": 10, "antecedentes": 10}
    },
    {
        "id": 7,
        "nombre": "Disciplina",
        "descripcion": "Físico +2, inteligencia +1",
        "efectos": {"apariencia": 0, "inteligencia": 1, "fisico": 2, "antecedentes": 0}
    },
    {
        "id": 8,
        "nombre": "Marcador de posición",
        "descripcion": "Aún no sabes qué eres...",
        "efectos": {"apariencia": 0, "inteligencia": 0, "fisico": 0, "antecedentes": 0}
    }
]


def mostrar_talentos():
    """Muestra todos los talentos disponibles."""
    from utils import caja, separador, BOLD, CYAN, RESET, BLANCO, AMARILLO
    
    print(f"\n{BOLD}{AMARILLO}🎲 TALENTOS DISPONIBLES{RESET}\n")
    for t in TALENTOS_DISPONIBLES:
        print(f"  {CYAN}[{t['id']}]{RESET} {BOLD}{t['nombre']}{RESET}")
        print(f"      {BLANCO}{t['descripcion']}{RESET}")
        ef = t['efectos']
        print(f"      Efectos: Apariencia {ef['apariencia']:+d}, Inteligencia {ef['inteligencia']:+d}, Físico {ef['fisico']:+d}, Antecedentes {ef['antecedentes']:+d}")
        print()
