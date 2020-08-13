# -*- coding: utf-8 -*

if __name__ == "__main__":
    # Variaveis
    tamanho_vetor = 10
    vetor = []

    while(tamanho_vetor > 0):
        # Entrada
        valor = int(input())

        # Seguindo restricoes para os valores
        # que sao adicionados corretamente no vetor
        if(valor <= 0):
            vetor.append(1)
        else:
            vetor.append(valor)

        tamanho_vetor -= 1

    # Resultado
    for i in range(0, len(vetor)):
        print("X[" + str(i) + "] = " + str(vetor[i]))