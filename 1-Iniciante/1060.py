# -*- coding: utf-8 -*

positivos = 0
for i in range(0, 6):
    valor = float(input())
    if (valor >= 0):
        positivos = positivos + 1

print(positivos, "valores positivos")