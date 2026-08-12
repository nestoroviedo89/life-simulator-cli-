# personaje.py
# Life Simulator v0.5.9


class Personaje:

    def __init__(
        self,
        edad,
        genero,
        atributos,
        talentos,
        historia,
        muerto=False
    ):
        self.edad = edad
        self.genero = genero
        self.atributos = atributos
        self.talentos = talentos
        self.historia = historia
        self.muerto = muerto

    # =========================
    # ESTADO DEL PERSONAJE
    # =========================

    def mostrar_estado(self):

        print("\n===== PERSONAJE =====")

        print("Edad:", self.edad)
        print("Género:", self.genero)

        print(
            "Apariencia:",
            self.atributos["apariencia"]
        )

        print(
            "Inteligencia:",
            self.atributos["inteligencia"]
        )

        print(
            "Físico:",
            self.atributos["fisico"]
        )

        print(
            "Antecedentes:",
            self.atributos["antecedentes"]
        )

    # =========================
    # NACIMIENTO
    # =========================

    def nacer(self):

        if self.atributos["antecedentes"] >= 10:

            familia = (
                "rico de segunda generación"
            )

        elif self.atributos["antecedentes"] >= 5:

            familia = (
                "en una familia adinerada"
            )

        else:

            familia = (
                "en una familia humilde"
            )

        texto = (
            f"[{self.edad} años: Naciste, "
            f"un {self.genero}, {familia}]"
        )

        self.historia.append(
            texto
        )

        return texto

    # =========================
    # ENVEJECER
    # =========================

    def envejecer(self):

        self.edad += 1

        return self.edad

    # =========================
    # APLICAR HERENCIA DEL ALMA
    # =========================

    def aplicar_herencia(self, herencia):

        for atributo in self.atributos:

            bonificacion = herencia.get(
                atributo,
                0
            )

            self.atributos[atributo] += (
                bonificacion
            )

    # =========================
    # CONVERTIR A DICCIONARIO
    # =========================

    def convertir_a_dict(self, nombre):

        return {
            "nombre": nombre,
            "edad": self.edad,
            "atributos": self.atributos,
            "genero": self.genero,
            "talentos": self.talentos,
            "historia": self.historia,
            "muerto": self.muerto
        }

    # =========================
    # RECONSTRUIR PERSONAJE
    # =========================

    @classmethod
    def desde_dict(cls, datos):

        return cls(
            edad=datos["edad"],
            genero=datos["genero"],
            atributos=datos["atributos"],
            talentos=datos["talentos"],
            historia=datos["historia"],
            muerto=datos.get(
                "muerto",
                False
            )
        )