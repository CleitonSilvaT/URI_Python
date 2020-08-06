# -*- coding: utf-8 -*

# Encontrar a soma dos proximos(j) elementos impares(i)
def calcular_soma(i, j):
    soma = 0

    while(j > 0):
        # Veriricando se i eh impar
        if(i % 2 == 1):
            soma += i
            j -= 1
        i += 1
    # Resultado
    print(soma)


if __name__ == '__main__':
    # Entrada n
    n = int(input())

    # Entrada casos de teste
    while(n > 0):
        valores = input()
        num = valores.split(" ")
        x = int(num[0])
        y = int(num[1])

        calcular_soma(x, y)
        n -= 1