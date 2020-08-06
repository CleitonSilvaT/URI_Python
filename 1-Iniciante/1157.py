# -*- coding: utf-8 -*

if __name__ == '__main__':
    # Entrada
    n = int(input())

    # Calcular os divisores de n
    for i in range(1, n+1):
        if(n % i == 0):
            print(i)