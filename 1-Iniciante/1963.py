# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    entrada = input()

    # Constantes
    valor_antigo = float(entrada.split(' ')[0])
    valor_novo = float(entrada.split(' ')[1])

    # Calculando a diferenca e percentual de aumento
    diferenca = valor_novo - valor_antigo
    aumento = (diferenca * 100) / valor_antigo

    # Resultado
    print('%.2f' % aumento + '%')