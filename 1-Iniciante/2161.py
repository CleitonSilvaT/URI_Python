# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    repeticoes = int(input())
    # Variavel
    resultado = 0
    if(repeticoes > 0):
        # Controlando a quantidade de repeticoes
        for i in range(repeticoes):
            resultado = 1/(resultado + 6)
    resultado = resultado + 3
    # Resultado
    print('%.10f' % resultado)