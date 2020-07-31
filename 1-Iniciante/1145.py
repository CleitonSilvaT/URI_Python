# -*- coding: utf-8 -*

# Imprimir valores na mesma linha
def imprimir(valor):
    print(valor, end=" ")

if __name__ == '__main__':
    # Entrada
    entrada = input()
    valores = entrada.split(" ")
    x = int(valores[0])
    y = int(valores[1])

    # Primeiro numero
    num = 1

    # Sequencia de 1 ate Y
    while (num <= y):
        # Imprimir na linha X numeros
        for j in range(1, x):
            imprimir(num)
            num += 1
        # Ultimo elemento da linha com quebra de linha
        print(num)
        num += 1