# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Variaveis
    linhas = 12
    colunas = 12
    # Numero de elementos acima da diagonal principal
    num_elementos = 66
    soma = 0

    # Entrada
    operacao = input()

    # Matriz
    m = []
    for i in range(linhas):
        # Linha da matriz
        line = []
        for j in range(colunas):
            # Entrada
            valor = float(input())
            line.append(valor)
            # Encontrando matriz principal
            if(i == j):
                # O valor de k deve ir ate i-1 - lembrar que range eh exclusivo
                for k in range(i):
                    soma += m[k][j]
        m.append(line)

    # Resultado
    if(operacao == 'S'):
        print('%.1f' % soma)

    elif(operacao == 'M'):
        print('%.1f' % (soma / num_elementos))