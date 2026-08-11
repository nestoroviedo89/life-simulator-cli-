# eventos.py — Eventos por edad con sistema de rareza

import random


# Pesos de rareza
PESOS_RAREZA = {
    "comun": 60,
    "raro": 30,
    "epico": 9,
    "legendario": 1
}


def elegir_evento(eventos):
    """Elige un evento considerando su rareza."""
    pesos = [PESOS_RAREZA[e.get("rareza", "comun")] for e in eventos]
    return random.choices(eventos, weights=pesos, k=1)[0]


def evento_infancia(atributos, genero, talentos):
    eventos = [
        {"texto": "Aprendiste a caminar sin caerte.", "efectos": {"fisico": 1}, "rareza": "comun"},
        {"texto": "Tu primer día de guardería. Lloraste.", "efectos": {}, "rareza": "comun"},
        {"texto": "Ganaste un concurso de dibujo en el jardín.", "efectos": {"inteligencia": 1}, "rareza": "raro"},
        {"texto": "Te caíste de un árbol. Te rompiste el brazo.", "efectos": {"fisico": -1}, "rareza": "comun"},
        {"texto": "Aprendiste a leer antes que tus compañeros.", "efectos": {"inteligencia": 2}, "rareza": "raro"},
        {"texto": "Te picó una abeja. Lloraste una hora.", "efectos": {}, "rareza": "comun"},
        {"texto": "Tu familia te llevó de vacaciones a la playa.", "efectos": {"apariencia": 1}, "rareza": "comun"},
        {"texto": "Te enfermaste gravemente de neumonía.", "efectos": {"fisico": -2}, "rareza": "raro"},
        {"texto": "Hiciste tu primera comunión / fiesta grande.", "efectos": {"apariencia": 1, "antecedentes": 1}, "rareza": "comun"},
        {"texto": "Tu abuela te enseñó a cocinar arepas.", "efectos": {"inteligencia": 1, "fisico": 1}, "rareza": "comun"},
        {"texto": "Perdiste un diente en un accidente de bicicleta.", "efectos": {"apariencia": -1}, "rareza": "comun"},
        {"texto": "Adoptaste un perro callejero. Lo llamaste Firulais.", "efectos": {"apariencia": 1}, "rareza": "comun"},
        {"texto": "Te ganaste un concurso de spelling bee.", "efectos": {"inteligencia": 1}, "rareza": "raro"},
        {"texto": "Una estrella fugaz cruzó el cielo. Pediste un deseo.", "efectos": {"apariencia": 2, "inteligencia": 2}, "rareza": "epico"},
        {"texto": "Descubriste que puedes mover objetos con la mente. (Bueno, casi)", "efectos": {"inteligencia": 3}, "rareza": "legendario"},
    ]
    
    # Eventos especiales por talentos
    if any(t["nombre"] == "Bebé prematuro" for t in talentos):
        eventos.append({"texto": "Tu cuerpo frágil no resistió una infección respiratoria. Falleciste.", "efectos": {"fisico": -99}, "rareza": "raro"})
    
    if any(t["nombre"] == "Rica segunda generación" for t in talentos):
        eventos.append({"texto": "Tu familia te matriculó en el colegio más caro del país.", "efectos": {"inteligencia": 2, "apariencia": 1}, "rareza": "comun"})
    
    if any(t["nombre"] == "Sistema Skyfall" for t in talentos):
        eventos.append({"texto": "Un misterioso sistema apareció en tu mente. Todo parece más fácil.", "efectos": {"inteligencia": 3, "fisico": 2, "apariencia": 2}, "rareza": "epico"})
    
    return elegir_evento(eventos)


def evento_adolescencia(atributos, genero, talentos):
    eventos = [
        {"texto": "Entraste a la secundaria. Nuevos amigos, nuevos problemas.", "efectos": {}, "rareza": "comun"},
        {"texto": "Te enamoraste por primera vez. Te dejaron.", "efectos": {"apariencia": -1}, "rareza": "comun"},
        {"texto": "Descubriste que eres bueno en matemáticas.", "efectos": {"inteligencia": 2}, "rareza": "comun"},
        {"texto": "Te uniste al equipo de fútbol / voleibol.", "efectos": {"fisico": 2}, "rareza": "comun"},
        {"texto": "Te hiciste un corte moderno. Te quedó bien.", "efectos": {"apariencia": 2}, "rareza": "comun"},
        {"texto": "Reprobaste un año. Tuviste que repetir.", "efectos": {"inteligencia": -1}, "rareza": "raro"},
        {"texto": "Tu familia perdió dinero en una estafa. Ahora son más pobres.", "efectos": {"antecedentes": -2}, "rareza": "raro"},
        {"texto": "Trabajaste medio tiempo para ayudar en casa.", "efectos": {"fisico": 1, "antecedentes": 1}, "rareza": "comun"},
        {"texto": "Ganaste un torneo regional de ajedrez.", "efectos": {"inteligencia": 3, "antecedentes": 2}, "rareza": "epico"},
        {"texto": "Te ofrecieron un papel en una serie de TV local.", "efectos": {"apariencia": 3, "antecedentes": 3}, "rareza": "legendario"},
    ]
    
    if atributos["inteligencia"] >= 8:
        eventos.append({"texto": "Ganaste una beca académica completa.", "efectos": {"inteligencia": 2, "antecedentes": 2}, "rareza": "raro"})
    
    if atributos["apariencia"] >= 8:
        eventos.append({"texto": "Te volviste popular en el colegio. Todos te conocen.", "efectos": {"apariencia": 2, "antecedentes": 1}, "rareza": "comun"})
    
    return elegir_evento(eventos)


def evento_adultez(atributos, genero, talentos):
    eventos = [
        {"texto": "Entraste a la universidad. Elegiste una carrera al azar.", "efectos": {"inteligencia": 1}, "rareza": "comun"},
        {"texto": "Conseguiste tu primer trabajo. El sueldo es bajo.", "efectos": {"antecedentes": 1}, "rareza": "comun"},
        {"texto": "Te casaste. Una boda modesta.", "efectos": {"apariencia": 1, "antecedentes": 1}, "rareza": "comun"},
        {"texto": "Tuviste tu primer hijo. La vida cambió.", "efectos": {"fisico": -1, "antecedentes": 1}, "rareza": "comun"},
        {"texto": "Invertiste en un negocio. Funcionó bien.", "efectos": {"antecedentes": 4}, "rareza": "raro"},
        {"texto": "Perdiste tu trabajo en un recorte. Meses difíciles.", "efectos": {"antecedentes": -2}, "rareza": "comun"},
        {"texto": "Te diagnosticaron una enfermedad crónica.", "efectos": {"fisico": -2}, "rareza": "raro"},
        {"texto": "Viajaste al extranjero por primera vez.", "efectos": {"inteligencia": 2, "apariencia": 1}, "rareza": "comun"},
        {"texto": "Te divorciaste. Un proceso largo y doloroso.", "efectos": {"apariencia": -1, "antecedentes": -1}, "rareza": "comun"},
        {"texto": "Compraste tu primera casa. Un logro.", "efectos": {"antecedentes": 2}, "rareza": "comun"},
        {"texto": "Abriste tu propio negocio. Funcionó mejor de lo esperado.", "efectos": {"antecedentes": 4, "inteligencia": 1}, "rareza": "raro"},
        {"texto": "Te estafaron con una pirámide. Perdiste ahorros.", "efectos": {"antecedentes": -3, "inteligencia": 1}, "rareza": "raro"},
        {"texto": "Te hiciste viral en redes por un video gracioso.", "efectos": {"apariencia": 3, "antecedentes": 1}, "rareza": "epico"},
        {"texto": "Ganaste la lotería. Tu vida cambió para siempre.", "efectos": {"antecedentes": 10}, "rareza": "legendario"},
    ]
    
    if atributos["inteligencia"] >= 12:
        eventos.append({"texto": "Te convertiste en un experto reconocido en tu campo.", "efectos": {"inteligencia": 3, "antecedentes": 4}, "rareza": "raro"})
    
    if atributos["fisico"] <= 2:
        eventos.append({"texto": "Tu salud decayó gravemente. Tuviste que dejar el trabajo.", "efectos": {"fisico": -2, "antecedentes": -3}, "rareza": "raro"})
    
    if any(t["nombre"] == "Rica segunda generación" for t in talentos):
        eventos.append({"texto": "Tu familia te regaló un departamento en la zona exclusiva.", "efectos": {"antecedentes": 5}, "rareza": "raro"})
    
    return elegir_evento(eventos)


def evento_vejez(atributos, genero, talentos):
    eventos = [
        {"texto": "Te jubilaste. Ahora tienes tiempo libre.", "efectos": {"fisico": -1}, "rareza": "comun"},
        {"texto": "Te volviste abuelo. Los nietos te alegran la vida.", "efectos": {"apariencia": 2}, "rareza": "comun"},
        {"texto": "Tu visión empeoró. Necesitas lentes.", "efectos": {"fisico": -1}, "rareza": "comun"},
        {"texto": "Escribiste un libro de memorias. Pocos lo leyeron.", "efectos": {"inteligencia": 1}, "rareza": "raro"},
        {"texto": "Te caíste en la ducha. Fractura de cadera.", "efectos": {"fisico": -3}, "rareza": "raro"},
        {"texto": "Ganaste un torneo de bingo en el club de la tercera edad.", "efectos": {"apariencia": 1}, "rareza": "comun"},
        {"texto": "Un periodista escribió un artículo sobre tu vida.", "efectos": {"apariencia": 2, "antecedentes": 2}, "rareza": "epico"},
        {"texto": "Descubriste el secreto de la felicidad. Nadie te creyó.", "efectos": {"inteligencia": 5, "apariencia": 5}, "rareza": "legendario"},
    ]
    
    if atributos["fisico"] <= 0:
        eventos.append({"texto": "Tu cuerpo no resistió más. Falleciste en paz.", "efectos": {"fisico": -99}, "rareza": "comun"})
    
    return elegir_evento(eventos)


def obtener_evento(edad, atributos, genero, talentos):
    if edad <= 12:
        return evento_infancia(atributos, genero, talentos)
    elif edad <= 17:
        return evento_adolescencia(atributos, genero, talentos)
    elif edad <= 59:
        return evento_adultez(atributos, genero, talentos)
    else:
        return evento_vejez(atributos, genero, talentos)


def aplicar_efectos(atributos, efectos):
    for key, valor in efectos.items():
        atributos[key] += valor
    if atributos["fisico"] <= 0:
        return Fals
        e
    return True
