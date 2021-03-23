# -*- coding: utf-8 -*-

# Nao eh necessario armazenar os valores da matriz (trecho comentado)
if __name__ == '__main__':
    # Constantes e Variaveis
    linhas = 12
    colunas = 12
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
            # Controlando area a direita
            if((j > i) and (j > diagonal_secundaria)):
                soma += valor
        # Controlando diagonal secundaria
        diagonal_secundaria -= 1
        # m.append(line)

    # Resultado
    if(operacao == 'S'):
        print('%.1f' % soma)

    elif(operacao == 'M'):
        print('%.1f' % (soma / num_elementos))