# -*- coding: utf-8 -*

if __name__ == '__main__':
    # Sequencia S
    # S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

    # Variaveis
    numerador = 1
    denominador = 1
    s = numerador / denominador

    # Calculando a Sequencia S ate o numerador 39
    while(numerador < 39):
        # Crecimento do numerador
        numerador += 2
        # Crescimento do denominador
        denominador = denominador * 2
        s +=  numerador / denominador

    # Resultado
    print("%.2f" % s)