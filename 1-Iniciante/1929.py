# -*- coding: utf-8 -*-

# Para encontrar as 3 varetas possiveis, iremos assumir que a + b > c
if __name__ == '__main__':
    # Variavel
    valores = []

    # Entrada
    entrada = input()
    num = entrada.split(' ')

    # Transformando a lista em inteiros
    for i in num:
        valores.append(int(i))

    # Ordenando os valores da lista
    valores.sort()

    # Para encontrar as 3 varetas, iremos assumir que:
    # Elas podem ser formadas pelas 3 menores varetas
    # Elas podem ser formadas pelas 3 maiores varetas
    if(valores[0] + valores[1] > valores[2]):
        print('S')

    elif(valores[1] + valores[2] > valores[3]):
        print('S')

    else:
        print('N')