# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    entrada = float(input())

    # Transformando numero no formato científico
    saida = "{:.4E}".format(entrada)

    # Realizando tratamento de sinais
    if((entrada >= 0) and (saida[0] != '-')):
        valor_impresso = '+' + saida
        print(valor_impresso)
    else:
        print(saida)