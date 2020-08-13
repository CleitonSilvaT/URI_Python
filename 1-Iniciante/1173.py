# -*- coding: utf-8 -*

if __name__ == '__main__':
    # Variaveis
    vetor = []

    # Entrada
    primeiro_elemento = int(input())
    vetor.append(primeiro_elemento)

    # Controlar a quantidade de elementos no vetor
    while(len(vetor) < 10):
        # Calculando o novo valor a ser inserido (dobro do numero anterior)
        novo_valor = vetor[len(vetor) - 1] * 2
        vetor.append(novo_valor)

    # Resultado
    for i in range(0, len(vetor)):
        print("N[" + str(i) + "] = " + str(vetor[i]))