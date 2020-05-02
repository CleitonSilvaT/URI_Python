# -*- coding: utf-8 -*

# Variaveis
i = 0
j = [1, 2, 3]

# Rodar para todos os valores de i ate 2
while (i <= 2):
    # Cada valor de j
    for num in j:
        # Resultado
        print("I=" + str(i), "J=" + str(num))
        # Calcular aumento de j
        indice = j.index(num)
        # Usar funcao round para arredondar soma de uma casa decimal
        atualizado = round(num + 0.2, 1)
        # Ajuste para numeros inteiros
        inteiro = str(atualizado).split(".")
        if (inteiro[1] == "0"):
            j[indice] = int(atualizado)
        else:
            j[indice] = atualizado

    # Calcular aumento de i
    # Usar funcao round para arredondar soma de uma casa decimal
    atualizado = round(i + 0.2, 1)
    # Ajuste para numeros inteiros
    inteiro = str(atualizado).split(".")
    if (inteiro[1] == "0"):
        i = int(atualizado)
    else:
        i = atualizado