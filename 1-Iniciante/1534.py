# -*- coding: utf-8 -*-

# Nao eh necessario armazenar os valores em matriz(trecho de codigo comentado)
if __name__ == '__main__':

    while(True):
        # Ponto de parada EOF
        try:
            # Entrada
            ordem_matriz = input()
        except EOFError:
            break

        # matriz = []
        for i in range(int(ordem_matriz)):
            # line = []
            for j in range(int(ordem_matriz)):
                # Regras para definicao dos valores da matriz
                if(j == (int(ordem_matriz) - 1 - i)):
                    # line.append(2)
                    print(2, end='')
                elif (i == j):
                    # line.append(1)
                    print(1, end='')
                else:
                    # line.append(3)
                    print(3, end='')
            # matriz.append(line)
            # Quebrando linha para linha da matriz
            print()