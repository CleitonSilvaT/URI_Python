# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    num_medidas = int(input())
    info = input()
    # Variavel
    queda = 0
    # Transformando lista de entrada para inteiros
    rotacoes = [int(i) for i in info.split(' ')]

    for i in range(1, num_medidas):
        # Identificando início da queda de velocidade
        if(rotacoes[i] < rotacoes[i-1]):
            # Ajuste no indice
            queda = i + 1
            break
    # Resultado
    print(queda)