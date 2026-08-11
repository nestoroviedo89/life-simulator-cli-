# eventos.py — Sistema de eventos por edad

import random


def evento_infancia(atributos, genero, talentos):
    """Eventos de 0 a 12 años."""
    eventos = [
        {"texto": "Aprendiste a caminar sin caerte.", "efectos": {"fisico": 1}},
        {"texto": "Tu primer día de guardería. Lloraste.", "efectos": {"apariencia": 0}},
        {"texto": "Ganaste un concurso de dibujo en el jardín.", "efectos": {"inteligencia": 1}},
        {"texto": "Te caíste de un árbol. Te rompiste el brazo.", "efectos": {"fisico": -1}},
        {"texto": "Aprendiste a leer antes que tus compañeros.", "efectos": {"inteligencia": 2}},
        {"texto": "Te picó una abeja. Lloraste una hora.", "efectos": {"fisico": 0}},
        {"texto": "Tu familia te llevó de vacaciones a la playa.", "efectos": {"apariencia": 1}},
        {"texto": "Te enfermaste gravemente de neumonía.", "efectos": {"fisico": -2}},
        {"texto": "Hiciste tu primera comunión / fiesta de cumpleaños grande.", "efectos": {"apariencia": 1, "antecedentes": 1}},
    ]
    
    # Eventos especiales por talentos
    if any(t["nombre"] == "Bebé prematuro" for t in talentos):
        eventos.append({"texto": "Tu cuerpo frágil no resistió una infección respiratoria. Falleciste.", "efectos": {"fisico": -99}})
    
    if any(t["nombre"] == "Rica segunda generación" for t in talentos):
        eventos.append({"texto": "Tu familia te matriculó en el colegio más caro del país.", "efectos": {"inteligencia": 2, "apariencia": 1}})
    
    if any(t["nombre"] == "Sistema Skyfall" for t in talentos):
        eventos.append({"texto": "Un misterioso sistema apareció en tu mente. Todo parece más fácil.", "efectos": {"inteligencia": 3, "fisico": 2, "apariencia": 2}})
    
    return random.choice(eventos)


def evento_adolescencia(atributos, genero, talentos):
    """Eventos de 13 a 17 años."""
    eventos = [
        {"texto": "Entraste a la secundaria. Nuevos amigos, nuevos problemas.", "efectos": {"apariencia": 0}},
        {"texto": "Te enamoraste por primera vez. Te dejaron.", "efectos": {"apariencia": -1}},
        {"texto": "Descubriste que eres bueno en matemáticas.", "efectos": {"inteligencia": 2}},
        {"texto": "Te uniste al equipo de fútbol / voleibol.", "efectos": {"fisico": 2}},
        {"texto": "Te hiciste un corte moderno. Te quedó bien.", "efectos": {"apariencia": 2}},
        {"texto": "Reprobaste un año. Tuviste que repetir.", "efectos": {"inteligencia": -1}},
        {"texto": "Tu familia perdió dinero en una estafa. Ahora son más pobres.", "efectos": {"antecedentes": -2}},
        {"texto": "Trabajaste medio tiempo para ayudar en casa.", "efectos": {"fisico": 1, "antecedentes": 1}},
    ]
    
    if atributos["inteligencia"] >= 8:
        eventos.append({"texto": "Ganaste una beca académica completa.", "efectos": {"inteligencia": 2, "antecedentes": 2}})
    
    if atributos["apariencia"] >= 8:
        eventos.append({"texto": "Te volviste popular en el colegio. Todos te conocen.", "efectos": {"apariencia": 2, "antecedentes": 1}})
    
    return random.choice(eventos)


def evento_adultez(atributos, genero, talentos):
    """Eventos de 18 a 59 años."""
    eventos = [
        {"texto": "Entraste a la universidad. Elegiste una carrera al azar.", "efectos": {"inteligencia": 1}},
        {"texto": "Conseguiste tu primer trabajo. El sueldo es bajo.", "efectos": {"antecedentes": 1}},
        {"texto": "Te casaste. Una boda modesta.", "efectos": {"apariencia": 1, "antecedentes": 1}},
        {"texto": "Tuviste tu primer hijo. La vida cambió.", "efectos": {"fisico": -1, "antecedentes": 1}},
        {"texto": "Invertiste en un negocio. Funcionó bien.", "efectos": {"antecedentes": 3}},
        {"texto": "Perdiste tu trabajo en un recorte. Meses difíciles.", "efectos": {"antecedentes": -2}},
        {"texto": "Te diagnosticaron una enfermedad crónica.", "efectos": {"fisico": -2}},
        {"texto": "Viajaste al extranjero por primera vez.", "efectos": {"inteligencia": 2, "apariencia": 1}},
        {"texto": "Te divorciaste. Un proceso largo y doloroso.", "efectos": {"apariencia": -1, "antecedentes": -1}},
        {"texto": "Compraste tu primera casa. Un logro.", "efectos": {"antecedentes": 2}},
    ]
    
    if atributos["inteligencia"] >= 12:
        eventos.append({"texto": "Te convertiste en un experto reconocido en tu campo.", "efectos": {"inteligencia": 3, "antecedentes": 4}})
    
    if atributos["fisico"] <= 2:
        eventos.append({"texto": "Tu salud decayó gravemente. Tuviste que dejar el trabajo.", "efectos": {"fisico": -2, "antecedentes": -3}})
    
    if any(t["nombre"] == "Rica segunda generación" for t in talentos):
        eventos.append({"texto": "Tu familia te regaló un departamento en la zona exclusiva.", "efectos": {"antecedentes": 5}})
    
    return random.choice(eventos)


def evento_vejez(atributos, genero, talentos):
    """Eventos de 60+ años."""
    eventos = [
        {"texto": "Te jubilaste. Ahora tienes tiempo libre.", "efectos": {"fisico": -1}},
        {"texto": "Te volviste abuelo. Los nietos te alegran la vida.", "efectos": {"apariencia": 2}},
        {"texto": "Tu visión empeoró. Necesitas lentes.", "efectos": {"fisico": -1}},
        {"texto": "Escribiste un libro de memorias. Pocos lo leyeron.", "efectos": {"inteligencia": 1}},
        {"texto": "Te caíste en la ducha. Fractura de cadera.", "efectos": {"fisico": -3}},
        {"texto": "Ganaste un torneo de bingo en el club de la tercera edad.", "efectos": {"apariencia": 1}},
    ]
    
    if atributos["fisico"] <= 0:
        eventos.append({"texto": "Tu cuerpo no resistió más. Falleciste en paz.", "efectos": {"fisico": -99}})
    
    return random.choice(eventos)


def obtener_evento(edad, atributos, genero, talentos):
    """Devuelve un evento según la edad del personaje."""
    if edad <= 12:
        return evento_infancia(atributos, genero, talentos)
    elif edad <= 17:
        return evento_adolescencia(atributos, genero, talentos)
    elif edad <= 59:
        return evento_adultez(atributos, genero, talentos)
    else:
        return evento_vejez(atributos, genero, talentos)


def aplicar_efectos(atributos, efectos):
    """Aplica los cambios de atributos y devuelve si el personaje sigue vivo."""
    for key, valor in efectos.items():
        atributos[key] += valor
    
    # Si físico llega a 0 o menos, muere
    if atributos["fisico"] <= 0:
        return False  # Muerto
    return True  # Vivo
