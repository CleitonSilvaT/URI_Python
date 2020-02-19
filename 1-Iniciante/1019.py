# -*- coding: utf-8 -*

# Recebe o valor inteiro em segundos
segundos = int(input())

# Converter o valor recebido em horas:minutos:segundos
horas = 0
minutos = 0

# A cada 60 segundos, equivale a 1 minuto
while segundos >= 60:
    # Encontrar os minutos proporcionais
    minutos = int(segundos / 60)
    # Atualizando o valor dos segundos restantes
    segundos = segundos - (minutos * 60)

    # A cada 60 minutos, equivale a 1 hora
    while minutos >= 60:
        # Encontrar as horas proporcionais
        horas = int(minutos / 60)
        # Atualizando o valor dos minutos restantes
        minutos = minutos - (horas * 60)

print(str(horas) + ":" + str(minutos) + ":" + str(segundos))