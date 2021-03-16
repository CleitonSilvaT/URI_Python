# -*- coding: utf-8 -*

if __name__ == '__main__':
    # Entrada
    n = int(input())
    valores = input()
    elementos = valores.split(' ')

    # Atribuindo o primeiro valor do vetor como sendo o menor
    menor = int(elementos[0])
    posicao = 0

    # Percorrer o vetor para verificar se existe algum elemento menor
    for i in range(1, n):
        if(int(elementos[i]) < menor):
            menor = int(elementos[i])
            posicao = i

    # Resultado
    print('Menor valor:', menor)
    print('Posicao:', posicao)