# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    entrada = input()
    num_linha = int(entrada.split(' ')[0])
    num_coluna = int(entrada.split(' ')[1])
    # Variaveis
    cord_x = 0
    cord_y = 0

    matriz = []
    # Contruindo a matriz
    for i in range(num_linha):
        # Entrada
        entrada = input()
        info = entrada.split(' ')
        line = []
        for j in range(num_coluna):
            valor = int(info[j])
            line.append(valor)
        matriz.append(line)
    # Buscando o sabre de luz
    for i in range(num_linha):
        for j in range(num_coluna):
            valor = matriz[i][j]
            # Garantindo o valor correto
            if(valor == 42):
                # Identificando se o valor possui todos os lados cobertos
                if((0 < i < num_linha-1) and (0 < j < num_coluna-1)):
                    # Identificando o padrao
                    if(matriz[i-1][j] == 7) and (matriz[i+1][j] == 7) and\
                      (matriz[i][j-1] == 7) and (matriz[i][j+1] == 7) and\
                      (matriz[i-1][j-1] == 7) and (matriz[i-1][j+1] == 7) and\
                      (matriz[i+1][j-1] == 7) and (matriz[i+1][j+1] == 7):
                        # Identificando posicoes, realizando ajuste considerando iniciar em 0
                        cord_x = i + 1
                        cord_y = j + 1
                        break
    # Resultado
    print(cord_x, cord_y)