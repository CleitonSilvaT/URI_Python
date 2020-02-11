# -*- coding: utf-8 -*

# Distancia dada em KM/h
x = 60
y = 90

# Transformando distância em KM/m
distanciaXporMinuto = x / 60
distanciaYporMinuto = y / 60

# Computar a diferença de distância entre os dois carros em cada minuto
diferencaPorMinuto = distanciaYporMinuto - distanciaXporMinuto

# Capturando a distância entre os dois carros
diferencaDistancia = int(input())

# Computar minutos gastos para atingir a diferença desejada
minutosGastos = int (diferencaDistancia / diferencaPorMinuto)

print(minutosGastos, "minutos")