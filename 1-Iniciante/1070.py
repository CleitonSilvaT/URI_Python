# -*- coding: utf-8 -*

# Entrada
num = int(input())

# Variável
impares = 0

# Calcular a quantidade de numeros impares impressos
while (impares < 6):
    # Identifica se o numero é impar, imprime e computa
    if (num % 2 != 0):
        print(num)
        impares = impares + 1

    # Avança para o próximo número
    num = num + 1