# -*- coding: utf-8 -*-

# Nao existe necessidade de armazenar toda a matriz (codigo comentado)
if __name__ == '__main__':
    # Constantes e Variaveis
    colunas = 12
    linhas = 12
    # Quantidade de valores que devem ser somados
    valores = 66
    # Lembrando que a posicao vai de 0 ate o valor
    diagonal_secundaria = colunas - 1
    soma = 0

    # Entrada
    operacao = input()

    # Matriz
    # m = []
    for i in range(linhas):
        # Cada linha da matriz
        line = []
        for j in range(colunas):
            # Entrada
            elemento = float(input())
            line.append(elemento)
            # Soma dos elementos acima da diagonal secundaria
            if(j == diagonal_secundaria):
                for k in range(j):
                    soma += line[k]
        diagonal_secundaria -= 1
        # m.append(line)

    # Resultado
    if(operacao == 'S'):
        print('%.1f' % soma)

    elif(operacao == 'M'):
        print('%.1f' % (soma / valores))