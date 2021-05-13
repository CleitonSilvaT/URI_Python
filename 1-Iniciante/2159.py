# -*- coding: utf-8 -*-
import math

if __name__ == '__main__':
    # Entrada
    numero = int(input())
    # Caculando valores seguindo a formula
    min_primo = numero / math.log(numero, math.e)
    max_primo = 1.25506 * (numero / math.log(numero, math.e))
    # Resultado
    print('{:.1f} {:.1f}'.format(min_primo, max_primo))