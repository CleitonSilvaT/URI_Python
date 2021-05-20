# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    mensagem_original = input()
    # Variavel
    nova_mensagem = ''
    # Contando quantidade de bits 1 da entrada
    quant_um = mensagem_original.count('1')
    # Atendendo a especificacao
    if (quant_um % 2 != 0):
        nova_mensagem = mensagem_original + '1'
    else:
        nova_mensagem = mensagem_original + '0'
    # Resultado
    print(nova_mensagem)