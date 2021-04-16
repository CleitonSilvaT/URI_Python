# -*- coding: utf-8 -*-

if __name__ == '__main__':
    while(True):
        # Condição de parada
        try:
            # Entrada
            num_lesmas = input()
        except(EOFError):
            break

        # Entrada
        e_velocidade = input()
        velocidades = e_velocidade.split(' ')

        lesma_rapida = 0

        # Encontrar a lesma mais rapida
        for lesma in velocidades:
            if (int(lesma) > lesma_rapida):
                lesma_rapida = int(lesma)

        # Classificando o nivel da lesma
        if(lesma_rapida < 10):
            print(1)
        elif(lesma_rapida < 20):
            print(2)
        else:
            print(3)