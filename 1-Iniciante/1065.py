# -*- coding: utf-8 -*

# Entrada
a1 = input()
a2 = input()
a3 = input()
a4 = input()
a5 = input()

# Variáveis
valores = []
par = 0

# Adicionando valores de entrada em uma lista (como elmentos float)
valores.append(float(a1))
valores.append(float(a2))
valores.append(float(a3))
valores.append(float(a4))
valores.append(float(a5))

# Encontrar quais elementos são pares
for i in valores:
    if (i % 2 == 0):
        par = par + 1

# Resultado
print(par, "valores pares")