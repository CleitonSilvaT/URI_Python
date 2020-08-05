# -*- coding: utf-8 -*

# Funcao para calcular fatorial
def fatorial(valor):
    if(valor <= 1):
        return 1
    else:
        return valor * fatorial (valor-1)

if __name__ == '__main__':

    # Entrada
    n = int(input())

    # Resultado
    print(fatorial(n))