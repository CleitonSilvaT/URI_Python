# -*- coding: utf-8 -*

if __name__ == '__main__':
    # Entrada
    n = int(input())

    # Variaveis
    sequencia = []
    valor = 0
    numeros = ""

    # Construindo a sequencia de Fibonacci em ordem crescente
    for i in range(0, n):
        # Definindo os primeros valores
        if(i <= 1):
            valor = i
        # Calculando os demais
        else:
            valor = sequencia[i-1] + sequencia[i-2]
        sequencia.append(valor)

    # Preparando valores no formato para serem impressos
    for num in sequencia:
        numeros = numeros + str(num) + " "

    # Resultado
    print(numeros[:-1])