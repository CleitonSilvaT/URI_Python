# -*- coding: utf-8 -*

entrada = input()

valores = entrada.split(" ")

hora_inicial = int(valores[0])
hora_final = int(valores[1])
dia = 24

# Se a hora inicial for menor que a final indica que será no mesmo dia
if (hora_inicial < hora_final):
    tempo = hora_final - hora_inicial

# Caso contrário a partida iniciou em um dia e terminou em outro
else:
    tempo = dia - hora_inicial + hora_final

print("O JOGO DUROU", tempo, "HORA(S)")