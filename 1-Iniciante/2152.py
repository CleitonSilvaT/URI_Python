# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    casos_teste = int(input())

    while(casos_teste > 0):
        info = input().split(' ')
        # Formatando resultado para sempre possuir dois digitos
        print('{:0>2}:{:0>2}'.format(info[0],info[1]), end='')
        if(info[2] == '0'):
            print(' - A porta fechou!')
        else:
            print(' - A porta abriu!')
        casos_teste -= 1