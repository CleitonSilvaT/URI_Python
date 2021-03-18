# -*- coding: utf-8 -*-

# Como nao foi exigido o armazenamento completo da matriz (trecho de codigo comentado)
# Decidi em usar apenas os valores de interesse (coluna desejada)
if __name__ == '__main__':
    # Variaveis
    linhas = 12
    colunas = 12
    soma = 0

    # Entrada
    coluna_desejada = int(input())
    operacao = input()

    # Matriz
    # m = []
    for i in range(linhas):
        # Cada linha da matriz
        # line = []
        for j in range(colunas):
            # Entrada de cada elemento
            valor = float(input())
            # line.append(valor)
            if(j == coluna_desejada):
                soma += valor
        # m.append(line)

    # Resultado
    if(operacao == 'S'):
        print('%.1f' % soma)

    elif(operacao == 'M'):
        print('%.1f' % (soma/linhas))