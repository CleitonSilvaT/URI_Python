# -*- coding: utf-8 -*-

# Nao eh necessario armazenar a matriz (trecho de codigo comentado)
if __name__ == '__main__':
    # Constantes e Variaveis
    colunas = 12
    linhas = 12
    num_elementos = 30
    diagonal_secundaria = colunas - 1
    soma = 0

    # Entrada
    operacao = input()

    # Matriz
    # m = []
    for i in range(linhas):
        # Cada linha da matriz
        # line = []
        for j in range(colunas):
            # Entrada
            valor = float(input())
            # line.append(valor)
            # Buscando apenas os elementos da Area Superior
            if((j > i) and (j < diagonal_secundaria)):
                soma += valor
        # Controlando diagonal secundaria
        diagonal_secundaria -= 1
        # m.append(line)

    # Resultado
    if(operacao == 'S'):
        print('%.1f' % soma)

    elif(operacao == 'M'):
        print('%.1f' % (soma / num_elementos))