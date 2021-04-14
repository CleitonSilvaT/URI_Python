# -*- coding: utf-8 -*-
# Importe para uso de raiz quadrada
import math

if __name__ == '__main__':
    # Entrada
    entrada = input()
    while(entrada != '0'):
        # Distinguindo valores
        medidas = entrada.split(' ')
        medida_a = int(medidas[0])
        medida_b = int(medidas[1])
        percentual_maximo = int(medidas[2])

        # Calculando lado para o terreno
        lado_terreno = math.sqrt((medida_a * medida_b) * (100 / percentual_maximo))

        # Resultado
        print(int(lado_terreno))

        # Entrada
        entrada = input()
