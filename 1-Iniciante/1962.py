# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    num_linhas = int(input())
    # Constante
    ano_base = 2015

    while(num_linhas > 0):
        # Entrada
        ano = int(input())
        # Encontrando o tempo transcorrido
        diferenca_tempo = ano_base - ano
        # Consideranco apenas que existe A.C. e D.C.
        # Sendo assim, nao existe 0 (zero)
        if(diferenca_tempo <= 0):
            diferenca_tempo -= 1

        # Distinguindo entre A.C. e D.C.
        if(diferenca_tempo > 0):
            print(diferenca_tempo,'D.C.')
        else:
            # Calculando modulo da diferenca para imprimir resultado
            print(abs(diferenca_tempo), 'A.C.')
        num_linhas -= 1