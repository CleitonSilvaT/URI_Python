# -*- coding: utf-8 -*-

# Nao eh necessario armazenar os dados em uma matriz (codigo comentado)
if __name__ == '__main__':
    while(True):
        # Condicao de parada
        try:
            entrada = input()
        except(EOFError):
            break

        ordem_matriz = int(entrada)
        # matriz = []
        quadro_interno = int(ordem_matriz / 3)
        for i in range(ordem_matriz):
            # line = []
            for j in range(ordem_matriz):
                # Ponto central da matriz
                if ((j == (ordem_matriz - 1 - i)) and (i == j)):
                    # line.append(4)
                    print(4, end='')
                # Quadro interno da matriz
                elif ((quadro_interno <= i <= (ordem_matriz - quadro_interno - 1)) and (quadro_interno <= j <= (ordem_matriz - quadro_interno - 1))):
                    # line.append(1)
                    print(1, end='')
                # Diagonal principal
                elif(i == j):
                    # line.append(2)
                    print(2, end='')
                    # Diagonal secundaria
                elif(j == (ordem_matriz - 1 - i)):
                    # line.append(3)
                    print(3, end='')
                else:
                    # line.append(0)
                    print(0, end='')
            # matriz.append(line)
            # Separando linhas da matriz
            print()
        # Espaco entre as matrizes
        print()