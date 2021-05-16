# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    repeticao = int(input())
    # Variavel
    calculo = 0
    # Calculando de acordo com numero de repeticoes
    for i in range(repeticao):
        calculo = 1 / (calculo + 2)
    # Resultado, somado com valor 1 da formula
    print('%.10f' % (calculo + 1))