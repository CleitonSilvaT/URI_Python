# -*- coding: utf-8 -*

if __name__ == '__main__':

    # Sequencia S
    # S = 1 + 1/2 + 1/3 + … + 1/100
    numerador = 1
    denominador = 1
    s = 0

    # Calcular a Sequencia S
    while(denominador <= 100):
        s += numerador/denominador
        denominador += 1

    # Resultado
    print("%.2f" % s)
