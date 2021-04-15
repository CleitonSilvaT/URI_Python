# -*- coding: utf-8 -*-

if __name__ == '__main__':
    num_sorteado = int(input())

    for i in range(num_sorteado):
        print('Ho', end='')
        if(i != (num_sorteado - 1)):
            print(' ', end='')
    print('!')