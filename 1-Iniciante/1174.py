# -*- coding: utf-8 -*

if __name__ == '__main__':
    # Variaveis
    vetor = []

    # Capturar os 100 valores do vetor
    while(len(vetor) < 100):
        # Entrada
        valor = float(input())
        vetor.append(valor)

        # Restricao para impressao dos valores
        if(valor <= 10):
            # Resultado
            print("A[" + str(len(vetor) - 1) + "] = %.1f" % valor)