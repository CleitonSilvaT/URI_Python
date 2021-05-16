# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    texto = input()
    # Resultado
    if(len(texto) <= 140):
        print('TWEET')
    else:
        print('MUTE')