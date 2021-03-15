# -*- coding: utf-8 -*-

# Imprimindo Lista Par
def imprime_par(lista):
    # Controlando impressao de acordo com a quantidade de elementos na lista
    for i in range(0, len(lista)):
        print('par[' + str(i) + '] = ' + str(lista[i]))

# Imprimindo Lista Impar
def imprime_impar(lista):
    # Controlando impressao de acordo com a quantidade de elementos na lista
    for i in range(0, len(lista)):
        print('impar[' + str(i) + '] = ' + str(lista[i]))

if __name__ == '__main__':
    # Variaveis
    controle = 15
    par = []
    impar = []

    while(controle > 0):
        # Entrada
        valor = int(input())

        # Identificando Par
        if(valor % 2 == 0):
            # Restricao de listas com 5 elementos
            if(len(par) < 5):
                par.append(valor)
            else:
                imprime_par(par)
                par = []
                par.append(valor)
        # Identidicando Impar
        else:
            # Restricao de listas com 5 elementos
            if(len(impar) < 5):
                impar.append(valor)
            else:
                imprime_impar(impar)
                impar = []
                impar.append(valor)

        controle -= 1

    # Impressao final de acordo com a ordem estabelecida
    imprime_impar(impar)
    imprime_par(par)