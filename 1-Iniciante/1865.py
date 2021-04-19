# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    tentativas = int(input())

    while(tentativas > 0):
        # Entrada
        entrada = input()
        tentativa_i = entrada.split(' ')
        # Considerar 0 - nome e 1 - forca

        # Considerar que somente Thor pode levantar o martelo
        if(tentativa_i[0] == 'Thor'):
            print('Y')
        else:
            print('N')

        tentativas -= 1