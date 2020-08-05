# -*- coding: utf-8 -*

if __name__ == '__main__':
    # Entrada
    x = int(input())
    z = int(input())

    # Ler valores ate que z seja maior que x
    while (z <= x):
        z = int(input())

    # Variaveis
    soma = 0
    valores = 0

    for i in range(x, z):
        # Condicao de parada
        if(soma > z):
            break
        # Somando valores ate que soma > z
        soma = soma + i
        # Contar quantos valores foram somados
        valores += 1

    # Resultado
    print(valores)