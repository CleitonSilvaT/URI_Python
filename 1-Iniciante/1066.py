# -*- coding: utf-8 -*

# Entrada
a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())

# Variáveis
valores = []
par = 0
impar = 0
positivo = 0
negativo = 0

# Adicionar elementos em uma lista
valores.append(a1)
valores.append(a2)
valores.append(a3)
valores.append(a4)
valores.append(a5)

# Computar dados
for i in valores:
    # Pares
    if (i % 2 == 0):
        par = par + 1

    # Impares
    else:
        impar = impar + 1

    # Positivos
    if (i > 0):
        positivo = positivo + 1

    # Negativos
    elif (i < 0):
        negativo = negativo + 1

# Resultado
print(par, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(positivo, "valor(es) positivo(s)")
print(negativo, "valor(es) negativo(s)")