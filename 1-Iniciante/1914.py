# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    casos_teste = int(input())

    while(casos_teste > 0):
        # Entrada
        dados = input()
        escolha = dados.split(' ')
        # nomepessoa1 - escolha[0]
        # escolhapessoa1 - escolha[1]
        # nomepessoa2 - escolha[2]
        # escolhapessoa2 - escolha[3]

        # Entrada
        valores = input()
        numeros = valores.split(' ')
        # Calculando soma dos valores
        total = int(numeros[0]) + int(numeros[1])

        # Identificando se a soma eh PAR ou IMPAR
        if((total % 2) == 0):
            # Imprimindo o vencedor
            if(escolha[1] == 'PAR'):
                print(escolha[0])
            else:
                print(escolha[2])
        else:
            # Imprimindo o vencedor
            if(escolha[1] == 'IMPAR'):
                print(escolha[0])
            else:
                print(escolha[2])

        casos_teste -= 1