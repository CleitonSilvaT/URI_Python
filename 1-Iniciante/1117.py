# -*- coding: utf-8 -*

if __name__ == '__main__':

    # Variaveis
    nota_valida = 0
    total = 0

    # Capturar duas notas validas
    while (nota_valida < 2):
        # Entrada
        nota = float(input())

        # Limite das notas
        if( 0 <= nota <= 10):
            nota_valida = nota_valida + 1
            total = total + nota

        else:
            print("nota invalida")

    else:
        # Computar media
        media = total / 2
        # Resultado
        print("media = %.2f" % media)