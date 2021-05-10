# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    casos_teste = int(input())
    numeros = input()
    # Transformando entrada em lista de inteiros
    lista_numeros = [int(i) for i in numeros.split(' ')]
    # Lista em que cada indice representa os multiplos de 2, 3, 4, 5, respectivamente
    multiplos = [0 for i in range(4)]

    # Encontrando os multiplos dos numeros buscados
    for valor in lista_numeros:
        if(valor % 2 == 0):
            multiplos[0] += 1
        if(valor % 3 == 0):
            multiplos[1] += 1
        if(valor % 4 == 0):
            multiplos[2] += 1
        if(valor % 5 == 0):
            multiplos[3] += 1
    # Resultado
    for i in range(len(multiplos)):
        print(multiplos[i], 'Multiplo(s) de', i + 2)