# -*- coding: utf-8 -*-

def construindo_extremidades(matriz, ordem_matriz, valor, diagonal_i, diagonal_j):
    for i in range(diagonal_i, ordem_matriz):
        for j in range(diagonal_j, ordem_matriz):
            if(matriz[i][j] == 0):
                if ((i == diagonal_i) or (i == (ordem_matriz - valor)) or
                    (j == diagonal_j) or (j == (ordem_matriz - valor))):
                    matriz[i][j] = valor


def imprimir_matriz(matriz, ordem_matriz):
    for i in range(ordem_matriz):
        for j in range(ordem_matriz):
            print('%3d' % matriz[i][j], end='')
            if (j != (ordem_matriz - 1)):
                print(' ', end='')
        print()

if __name__ == '__main__':
    # Variavel
    nivel = 0

    # Entrada
    ordem_matriz = int(input())

    # Continuando a execução
    while(ordem_matriz != 0):

        # Construindo matriz com valores 0
        matriz = []
        for i in range(ordem_matriz):
            line = []
            for j in range(ordem_matriz):
                line.append(0)
            matriz.append(line)

        # Navegando pela matriz e construindo suas extremidades
        for i in range(ordem_matriz):
            for j in range(ordem_matriz):
                #  Considerando a diagonal principal para definir o ponto de inicio da construcao das extremidades
                if((i == j) and (matriz[i][j] == 0)):
                    nivel += 1
                    diagonal_i = i
                    diagonal_j = j
                    construindo_extremidades(matriz, ordem_matriz, nivel, diagonal_i, diagonal_j)
                    # Somente eh necessario identificar o primeiro elemento que faz parte da diagonal principal
                    # que nao foi preenchido
                    break

        # Imprimir matriz de acordo com formato
        imprimir_matriz(matriz, ordem_matriz)
        # Imprimir linha separando matrizes
        print()
        # Capiturando proxima entrada
        ordem_matriz = int(input())