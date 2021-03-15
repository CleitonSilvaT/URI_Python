# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Variaveis
    entrada = float(input())
    limite = 0

    # Controlando a quantidade de impressoes
    while(limite < 100):
        # Resposta
        print('N[' + str(limite) + '] = %.4f' % entrada)
        limite += 1
        # Calculando o proximo valor
        entrada = entrada / 2