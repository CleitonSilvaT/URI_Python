# -*- coding: utf-8 -*

# Entrada
num = int(input())

# Caminhar por todos os numeros de 1 até num
for i in range(1, num + 1):
    # Identificar se o elemento é ímpar
    if(i % 2 != 0):
        print(i)