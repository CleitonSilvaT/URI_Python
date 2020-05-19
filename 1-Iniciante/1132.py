# -*- coding: utf-8 -*

if __name__ == '__main__':
    # Variaveis
    soma = 0

    # Entrada
    x = int(input())
    y = int(input())

    # Sempre colocar x (maior) e y (menor)
    if (y < x):
        temp = y
        y = x
        x = temp

    # Identificar numeros que nao sao multiplos de 13 (x ate y)
    for i in range(x, y+1):
        if (i % 13 != 0):
            soma = soma + i

    # Resultado
    print(soma)