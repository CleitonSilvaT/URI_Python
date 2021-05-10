# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Variavel
    caso = 0

    while(True):
        # Controlando o caso de teste
        caso += 1
        # Condicao de parada
        try:
            # Entrada
            num_1 = input()
            num_2 = input()
        except(EOFError):
            break

        print('Caso #' + str(caso) + ':')
        if(num_1 in num_2):
            print('Qtd.Subsequencias: ', end='')
            # Funcao count encontra a quantidade total de substrings
            print(num_2.count(num_1))

            print('Pos: ', end='')
            # Funcao rfind encontra posicao da ultima substring, realizado ajuste do inicio de contagem de 0 para 1
            print(num_2.rfind(num_1) + 1)
        else:
            print('Nao existe subsequencia')
        # Separando entradas
        print()