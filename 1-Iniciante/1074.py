# -*- coding: utf-8 -*

# Variáveis
valores = []

# Entrada
n = int(input())
while (n > 0):
    valores.append(int(input()))
    n = n - 1

# Verificar para cada valor
for i in valores:
    if (i == 0):
        print("NULL")
    # Par
    elif(i % 2 == 0):
        # Positivo
        if(i > 0):
            print("EVEN POSITIVE")
        # Negativo
        else:
            print("EVEN NEGATIVE")
    # Impar
    else:
        # Positivo
        if(i > 0):
            print("ODD POSITIVE")
        # Negativo
        else:
            print("ODD NEGATIVE")