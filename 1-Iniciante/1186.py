# -*- coding: utf-8 -*-

# Nao eh necessario armazenar os dados da matriz (Trecho de codigo comentado)
if __name__ == '__main__':
    # Constantes e Variaveis
    colunas = 12
    linhas = 12
    valores = 66
    diagonal_secundaria = colunas
    soma = 0

    # Entrada
    operacao = input()

    # Matriz
    # m = []
    for i in range(linhas):
        line = []
        for j in range(colunas):
            # Elemento
            elemento = float(input())
            # line.append(elemento)
            # Buscando apenas elementos abaixo da diagonal secundaria
            if(j >= diagonal_secundaria):
                soma += elemento
        # Controlando diagonal secundaria
        diagonal_secundaria -= 1
        # m.append(line)

    # Resultado
    if(operacao == 'S'):
        print('%.1f' % soma)

    elif(operacao == 'M'):
        print('%.1f' % (soma / valores))