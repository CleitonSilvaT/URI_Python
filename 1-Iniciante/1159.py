# -*- coding: utf-8 -*

def calcula_soma(x):
    # Variaveis
    consecutivos = 5
    soma = 0

    while(consecutivos > 0):
        # Verificando valor par
        if(x % 2 == 0):
            soma += x
            consecutivos -= 1
        x += 1
    # Resultado
    print(soma)

if __name__ == '__main__':
    # Entrada
    x = int(input())

    # Capturando entrada ate encontrar valor 0
    while(x != 0):
        calcula_soma(x)
        x = int(input())