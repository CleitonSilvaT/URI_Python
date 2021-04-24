# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    entrada = input()
    cartas = entrada.split(' ')

    # A melhor opcao sera tirar uma carta igual a maior que ja possui na mao
    if(int(cartas[0]) >= int(cartas[1])):
        print(cartas[0])
    else:
        print(cartas[1])