# -*- coding: utf-8 -*

# Conforme foi mencionado que apenas era necessário realizar operações
# com a linha desejada, desconsiderei a construção da matriz (trecho de código comentado)
if __name__ == '__main__':
    # Variaveis
    linhas = 12
    colunas = 12
    soma = 0

    # Entradas
    linha = int(input())
    operacao = input()

    # Construindo a matriz
    # m = []
    for i in range(linhas):
        # Contruindo linha auxiliar
        # line = []
        for j in range(colunas):
            # Entrada da matriz
            valor = float(input())
            # line.append(valor)
            # Somando elementos da linha desejada
            if (i == linha):
                soma += valor
        # Adicionando linha completa na matriz
        # m.append(line)

    if(operacao == 'S'):
        print('%.1f' % soma)

    elif(operacao == 'M'):
        print('%.1f' % (soma/colunas))