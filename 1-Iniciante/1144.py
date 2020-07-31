# -*- coding: utf-8 -*

# Entrada
n = int(input())

# Sempre inicia com numero 1
primeiro = 1

# Cada linha deve conter 3 numeros
for i in range(0, n):
    # A sequencia segue duas linhas em conjunto:
    # Primeira - (primeiro numero e elevar primeiro numero ao quadrado e ao cubo)
    segundo = primeiro ** 2
    terceiro = primeiro ** 3
    print(primeiro, segundo, terceiro)

    # Segunda - (repetir primeiro numero e somar +1 aos demais da primeira linha)
    print(primeiro, segundo + 1, terceiro + 1)

    # Atualizar valor para proxima linha
    primeiro += 1