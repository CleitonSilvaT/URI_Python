# -*- coding: utf-8 -*

# Consumo KM/L
consumo = 12

# Tempo gasto em H
tempo = int(input())

# Velocidade média KM/H
velocidade = int(input())

litros = velocidade * tempo / consumo

print("%.3f" % litros)