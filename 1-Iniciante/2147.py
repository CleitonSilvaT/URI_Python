# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    casos_teste = int(input())

    while(casos_teste > 0):
        # Entrada
        palavra = input()
        tempo = 0.01 * len(palavra)
        # Resultado
        print('%.2f' % tempo)
        casos_teste -= 1