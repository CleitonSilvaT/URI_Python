# -*- coding: utf-8 -*

# Encontrar todos os dividores de um numero
def calcula_divisores(valor):
    num_divisores = []

    for i in range(1, valor):
        if(valor % i == 0):
            num_divisores.append(i)

    return num_divisores

# Soma valores de uma lista
def calcula_soma(num):
    soma = 0

    for i in num:
        soma += i

    return soma

if __name__ == '__main__':
    # Variaveis
    divisores = []
    soma_divisores = 0

    # Entrada
    casos_teste = int(input())

    while(casos_teste > 0):
        numero = int(input())

        divisores = calcula_divisores(numero)
        soma_divisores = calcula_soma(divisores)

        # Resultado
        if(numero == soma_divisores):
            print(str(numero), "eh perfeito")

        else:
            print(str(numero), "nao eh perfeito")

        casos_teste -= 1