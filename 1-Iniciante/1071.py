# -*- coding: utf-8 -*

# Entrada
x = int(input())
y = int(input())

# Variáveis
soma = 0

# Preservar ordem x < y
if (x > y):
    z = x
    x = y
    y = z

# Percorrer valores entre x e y
for i in range(x + 1 , y):
    # Verifica elementos impares
    if (i % 2 != 0):
        soma = soma + i

# Resultado
print(soma)