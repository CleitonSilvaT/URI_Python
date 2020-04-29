# -*- coding: utf-8 -*

# Capturar entrada
a1 = input()
a2 = input()
a3 = input()
a4 = input()
a5 = input()
a6 = input()

# Inicializar variáveis que serão utilizadas
positivos = 0
soma = 0
valores = []

# Adicionar elementos na lista (todos como float)
valores.append(float(a1))
valores.append(float(a2))
valores.append(float(a3))
valores.append(float(a4))
valores.append(float(a5))
valores.append(float(a6))

# Caminhar por todos os elementos da lista
for i in valores:
    # Computar quantos são positivos e a soma entre eles
    if (i >= 0):
        positivos = positivos + 1
        soma = soma + i

# Calcular a media dos elementos positivos
media = soma / positivos

# Resultado
print(positivos, "valores positivos")
print("%.1f" % media)