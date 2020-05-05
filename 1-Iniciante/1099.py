# -*- coding: utf-8 -*

# Variaveis
caso_teste = []
soma_impares = 0

# Entrada
n = int(input())

while (n > 0):
    caso_teste.append(input())
    n = n - 1

# Para cada caso de teste informado
for teste in caso_teste:
    soma_impares = 0
    elementos = teste.split(" ")
    # Representar x e y em ordem crescente
    if (int(elementos[0]) > int(elementos[1])):
        x = int(elementos[1])
        y = int(elementos[0])
    else:
        x = int(elementos[0])
        y = int(elementos[1])

    # Navegar nos elementos entre x e y
    for i in range(x + 1, y):
        # Verificar se eh impar
        if (i % 2 != 0):
            # Somar
            soma_impares = soma_impares + i
    # Resultado
    print(soma_impares)