# -*- coding: utf-8 -*

if __name__ == '__main__':

    # Variaveis
    vetor = []
    meio = 0

    # Capturar todos os valores de entrada
    while(len(vetor) < 20):
        valor = int(input())
        vetor.append(valor)

    meio = int(len(vetor)/2)

    # Ao percorrer a metada da lista, todos os elementos já terao sido alterados
    for i in range(0, meio):
        temp = vetor[i]
        vetor[i] = vetor[len(vetor) - 1 - i]
        vetor[len(vetor) - 1 - i]  = temp

    # Resultado
    for i in range(0, len(vetor)):
        print("N[" + str(i) + "] = " + str(vetor[i]))

