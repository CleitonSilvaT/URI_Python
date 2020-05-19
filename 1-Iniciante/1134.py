# -*- coding: utf-8 -*

if __name__ == '__main__':
    # Variaveis
    alcool = 0
    gasolina = 0
    diesel = 0

    while(True):
        # Entrada
        valor = int(input())

        # Computar valores
        if (valor == 1):
            alcool = alcool + 1

        elif (valor == 2):
            gasolina = gasolina + 1

        elif (valor == 3):
            diesel = diesel + 1

        elif (valor == 4):
            break

    # Resultado
    print("MUITO OBRIGADO")
    print("Alcool:", alcool)
    print("Gasolina:", gasolina)
    print("Diesel:", diesel)