# -*- coding: utf-8 -*

if __name__ == '__main__':
    # Variaveis
    lista_idades = []
    soma = 0

    # Entrada
    idade = int(input())

    # Capiturar idades enquanto o valor nao for negativo
    while(idade > 0):
        lista_idades.append(idade)
        idade = int(input())

    # Somar os valores das idades fornecidas
    for i in lista_idades:
        soma += i

    # Encontrar a media das idades
    media = soma / len(lista_idades)

    # Resultado
    print("%.2f" % media)