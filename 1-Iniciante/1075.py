# -*- coding: utf-8 -*

# Entrada
n = int(input())

# Percorrer numeros de 1 ate 10000
for i in range(1, 10000 + 1):
    # Resto da divisao com n igual a 2
    if (i % n == 2):
        # Resultado
        print(i)