# -*- coding: utf-8 -*-

if __name__ == '__main__':

    while(True):
        try:
            entrada = input()
        except(EOFError):
            break

        if(int(entrada) == 0):
            print('vai ter copa!')
        else:
            print('vai ter duas!')