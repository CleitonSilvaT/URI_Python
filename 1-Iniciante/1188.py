# -*- coding: utf-8 -*-

# Nao eh necessario armazenas a matriz (trecho de codigo comentado)
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
        # Separando cada linha da matriz
        # line = []
        for j in range(colunas):
            # Entrada
            valor = float(input())
            # line.append(valor)
            # Controlando apenas os elementos da parte inferior
            if((j > diagonal_secundaria) and (j < i)):
                soma += valor
        # Controlando diagonal secundaria
        diagonal_secundaria -= 1
        # m.append(line)

    # Resultado
    if(operacao == 'S'):
        print('%.1f' % soma)

    elif(operacao == 'M'):
        print('%.1f' % (soma / num_elementos))