# -*- coding: utf-8 -*

# Variável
potencia = 2

# Entrada
n = int(input())

# Rodar rodos os elementos de 1 até N
for i in range(1, n + 1):
    # Verificar se o elemento é par
    if (i % 2 == 0):
        # Resultado
        print(str(i) + "^" + str(potencia), "=", i**potencia)