# -*- coding: utf-8 -*

# Impressao da sequencia com a soma
def computar_resultado(m, n):
    soma = 0
    # Computar valores de m ate n
    for i in range(m, n + 1):
        # Somar valores
        soma = soma + i
        # Imprimir a lista
        imprimir_resultado(i)

    # Imprimir a soma dos elementos
    print("Sum=" + str(soma))

# Imprimir diferentes valores na mesma linha
def imprimir_resultado(texto):
    print(texto, end=" ")


if __name__ == '__main__':

    while(True):
        # Entrada
        entrada = input()
        valores = entrada.split(" ")

        # Se a entrada for menor ou igual a 0 para a execucao
        if (int(valores[0]) <= 0 or int(valores[1]) <= 0):
            break

        # Manter ordem m - menor elemento e n - maior elemento
        elif (int(valores[0]) > int(valores[1])):
            m = int(valores[1])
            n = int(valores[0])

        else:
            m = int(valores[0])
            n = int(valores[1])

        # Impressao da sequencia com a soma
        computar_resultado(m, n)


