# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    valor = int(input())
    # Formula para calcular raiz quadrada de n = n**0.5
    # Utilizando fórmula de Binet para calcular Fibonacci de um numero
    fibonacci = ((((1+(5**0.5))/2)**valor) - (((1-(5**0.5))/2)**valor))/5**0.5
    # Resultado
    print('%.1f' % fibonacci)