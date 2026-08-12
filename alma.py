# alma.py
# Life Simulator v0.6.0
# Sistema de alma, herencia, recuerdos y reencarnación


class Alma:

    def __init__(self):

        # Número de vidas completadas
        self.vidas_vividas = 0

        # Número de la vida actual
        self.vida_actual = 1

        # Recuerdos de vidas anteriores
        self.recuerdos = []

        # Características que pueden heredarse
        self.herencia = {
            "apariencia": 0,
            "inteligencia": 0,
            "fisico": 0,
            "antecedentes": 0
        }

        # Talentos que pueden pasar a futuras vidas
        self.talentos_heredados = []

    # =========================
    # REGISTRAR UNA VIDA
    # =========================

    def registrar_vida(
        self,
        edad,
        atributos,
        talentos
    ):

        self.vidas_vividas += 1

        recuerdo = {
            "vida": self.vidas_vividas,
            "edad_muerte": edad,
            "atributos": atributos.copy(),
            "talentos": talentos.copy()
        }

        self.recuerdos.append(
            recuerdo
        )

        self.calcular_herencia(
            atributos
        )

        self.guardar_talentos(
            talentos
        )

    # =========================
    # CALCULAR HERENCIA
    # =========================

    def calcular_herencia(
        self,
        atributos
    ):

        for atributo in self.herencia:

            valor = atributos.get(
                atributo,
                0
            )

            bonificacion = valor // 10

            self.herencia[atributo] = min(
                self.herencia[atributo] + bonificacion,
                10
            )

    # =========================
    # GUARDAR TALENTOS
    # =========================

    def guardar_talentos(
        self,
        talentos
    ):

        for talento in talentos:

            if talento not in self.talentos_heredados:

                self.talentos_heredados.append(
                    talento
                )

    # =========================
    # OBTENER HERENCIA
    # =========================

    def obtener_herencia(self):

        return self.herencia.copy()

    # =========================
    # NUEVA VIDA
    # =========================

    def nueva_vida(self):

        self.vida_actual += 1

        return self.vida_actual

    # =========================
    # MOSTRAR ALMA
    # =========================

    def mostrar(self):

        print("\n")
        print("========== ALMA ==========")

        print(
            "Vidas vividas:",
            self.vidas_vividas
        )

        print(
            "Vida actual:",
            self.vida_actual
        )

        print("\nHerencia:")

        for atributo, valor in self.herencia.items():

            print(
                f"  {atributo.capitalize()}: +{valor}"
            )

        print("\nTalentos heredados:")

        if self.talentos_heredados:

            for talento in self.talentos_heredados:

                if isinstance(talento, dict):

                    print(
                        f"  - {talento.get('nombre', 'Talento')}"
                    )

                else:

                    print(
                        f"  - {talento}"
                    )

        else:

            print(
                "  Ninguno"
            )

        print("\nRecuerdos:")

        if self.recuerdos:

            for recuerdo in self.recuerdos:

                print(
                    f"  Vida {recuerdo['vida']}: "
                    f"vivió {recuerdo['edad_muerte']} años"
                )

        else:

            print(
                "  Ninguno"
            )

        print(
            "=========================="
        )

    # =========================
    # CONVERTIR ALMA A DICT
    # =========================

    def convertir_a_dict(self):

        return {
            "vidas_vividas": self.vidas_vividas,
            "vida_actual": self.vida_actual,
            "recuerdos": self.recuerdos,
            "herencia": self.herencia,
            "talentos_heredados":
                self.talentos_heredados
        }

    # =========================
    # RECONSTRUIR ALMA
    # =========================

    @classmethod
    def desde_dict(cls, datos):

        alma = cls()

        alma.vidas_vividas = datos.get(
            "vidas_vividas",
            0
        )

        alma.vida_actual = datos.get(
            "vida_actual",
            1
        )

        alma.recuerdos = datos.get(
            "recuerdos",
            []
        )

        herencia_guardada = datos.get(
            "herencia",
            {}
        )

        for atributo in alma.herencia:

            alma.herencia[atributo] = (
                herencia_guardada.get(
                    atributo,
                    0
                )
            )

        alma.talentos_heredados = datos.get(
            "talentos_heredados",
            []
        )

        return alma

    # =========================
    # RESUMEN
    # =========================

    def resumen(self):

        return self.convertir_a_dict()