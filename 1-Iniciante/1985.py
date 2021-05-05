# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Tabela de precos
    produtos = {
        1001 : 1.5,
        1002 : 2.5,
        1003 : 3.5,
        1004 : 4.5,
        1005 : 5.5
    }
    # Variavel
    total = 0
    # Entrada
    num_produtos = int(input())

    while(num_produtos > 0):
        compra = input()
        cod_produto = int(compra.split(' ')[0])
        quantidade = int(compra.split(' ')[1])
        # Computando valor por item
        total += produtos[cod_produto] * quantidade

        num_produtos -= 1
    # Resultado
    print('%.2f' % total)