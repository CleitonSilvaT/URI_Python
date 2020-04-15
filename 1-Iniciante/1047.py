# -*- coding: utf-8 -*

entrada = input()

valores = entrada.split(" ")

hora_inicial = int(valores[0])
minuto_inicial = int(valores[1])

hora_final = int(valores[2])
minuto_final = int(valores[3])

tempo_minuto = 0
tempo_hora = 0

def tempo_corrente(inicial, final):
    return final - inicial

def tempo_limite_hora(inicial, final):
    dia = 24
    return dia - inicial + final

def tempo_limite_minuto(inicial, final):
    hora = 60
    return hora - inicial + final

if (minuto_inicial < minuto_final):

    tempo_minuto = tempo_corrente(minuto_inicial, minuto_final)

    if (hora_inicial == hora_final):
        tempo_hora = 0

    elif (hora_inicial < hora_final):
        tempo_hora = tempo_corrente(hora_inicial, hora_final)

    else:
        tempo_hora = tempo_limite_hora(hora_inicial, hora_final) - 1

else:
    tempo_minuto = tempo_limite_minuto(minuto_inicial, minuto_final)

    if (hora_inicial < hora_final):
        tempo_hora = tempo_corrente(hora_inicial, hora_final) - 1

    else:
        tempo_hora = tempo_limite_hora(hora_inicial, hora_final) - 1

# Ajustes de minutos / horas
if(tempo_minuto == 60):
    # Limite de duração máxima de 24 horas
    if (tempo_hora < 24):
        tempo_hora = tempo_hora + 1

    tempo_minuto = 0


print("O JOGO DUROU", tempo_hora, "HORA(S) E", tempo_minuto, "MINUTO(S)")