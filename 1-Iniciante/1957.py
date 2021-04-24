# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    num_decimal = int(input())

    # Transformando numero para hexadecimal
    num_hexadecimal = hex(num_decimal)

    # Resultado com letras em maiusculo
    print(num_hexadecimal[2:].upper())