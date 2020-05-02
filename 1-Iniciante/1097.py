# -*- coding: utf-8 -*

# Variaveis
i = 1
j = [7, 6, 5]

# Rodar para todos os valores de i ate 9
while (i <= 9):
    # Buscar cada elemento em j
    for num in j:
        # Resposta
        print("I=" + str(i), "J=" + str(num))
        # Atualizar valores em j
        indice = j.index(num)
        j[indice] = num + 2

    # Atualizar valor de i
    i = i + 2