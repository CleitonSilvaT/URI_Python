# -*- coding: utf-8 -*

if __name__ == '__main__':
    # Entrada
    entrada = input()

    valores = entrada.split(" ")

    a = int(valores[0])

    j = 1
    n = 0

    # Encontrar valor valido de N
    while(n <= 0):
        n = int(valores[j])
        j += 1

    # para i = 0 somar apenas a
    soma = a
    i = 1
    # 0 <= i <= N-1
    while(i <= n-1):
        # Soma de a para cada i
        soma = soma + a + i
        i+=1

    print(soma)