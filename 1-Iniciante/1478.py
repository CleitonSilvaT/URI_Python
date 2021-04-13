# -*- coding: utf-8 -*-

# Nao eh necessario armazenar os dados da matriz (codigo comentado)
if __name__ == '__main__':
    # Entrada
    ordem_matriz = int(input())

    # Construindo a Matriz
    while(ordem_matriz != 0):
        # matriz = []
        for i in range(ordem_matriz):
            # linha = []
            for j in range(ordem_matriz):
                # Atribuindo os valores seguindo o padrao
                if(i == j):
                    valor = 1
                elif(i > j):
                    valor = i - j + 1
                elif(j > i):
                    valor = j - i + 1

                # Imprimindo valores de acordo com o padrao
                print('%3d' % valor, end='')
                if (j != ordem_matriz - 1):
                    print(' ', end='')
                # linha.append(valor)
            # Saltar cada linha da matriz
            print()
            # matriz.append(linha)
        # Espaco entre matrizes
        print()
        # Entrada
        ordem_matriz = int(input())
