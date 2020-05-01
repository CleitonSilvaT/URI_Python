# -*- coding: utf-8 -*

# Variavel
testes = []
pesos = [2, 3, 5]
soma_pesos = 2 + 3 + 5

# Entrada
n = int(input())

while (n > 0):
    testes.append(input())
    n = n - 1

# Identificar os n casos de teste
for caso in testes:
    # Separ os valores reais
    elementos = caso.split(" ")
    # Computar a soma dos valores com seus pesos
    media_ponderada = pesos[0] * float(elementos[0]) + pesos[1] * float(elementos[1]) + pesos[2] * float(elementos[2])
    # Calcular a media ponderada
    media = media_ponderada / soma_pesos
    # Resultado
    print("%.1f" % media)
