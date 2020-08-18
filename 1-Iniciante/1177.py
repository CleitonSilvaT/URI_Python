# -*- coding: utf-8 -*

# Conforme a definicao do problema nao exige que o valor seja armazena
# A resposta eh calculada e apresentada diretamente

if __name__ == '__main__':
    # Variaveis
    limite = 1000
    contador = 0
    valor_temp = 0

    # Entrada
    valor = int(input())

    # Controlar o calculo ate 1000
    while(limite > contador):
        # Controlar a definicao dos valores de 0 ate n-1
        if (valor_temp == valor):
            valor_temp = 0

        # Imprimir resposta
        print("N[" + str(contador) + "] = " + str(valor_temp))
        valor_temp += 1
        contador += 1
