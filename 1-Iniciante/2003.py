# -*- coding: utf-8 -*-

if __name__ == '__main__':
    while(True):
        # Condicao de parada
        try:
            # Entrada
            entrada = input()
        except(EOFError):
            break
        # Identificando hora e minuto
        hora = int(entrada.split(':')[0])
        minutos = int(entrada.split(':')[1])
        # Computando tempo maximo para chegar no terminal
        hora += 1

        atraso = 0

        if(hora < 8):
            print('Atraso maximo:', atraso)
        else:
            # Computar atraso - em minutos
            atraso = (hora - 8) * 60
            print('Atraso maximo:', atraso + minutos)
