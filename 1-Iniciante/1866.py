# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    casos_teste = int(input())

    while(casos_teste > 0):
        # Entrada
        quantidade_termos = int(input())
        # Variaveis
        soma = 0
        i = 0
        # Realizando as devidas somas de acordo com os termos
        while(i < quantidade_termos):
            if(i == quantidade_termos - 1):
                soma += 1
                i += 1
            else:
                soma += 1
                soma -= 1
                i += 2
        # Resultado
        print(soma)

        casos_teste -= 1