# -*- coding: utf-8 -*-

# Para identificar o valor do menor circulo em englobe ambos
# eh necessario somar o valor do raio de ambosss
if __name__ == '__main__':
    casos_teste = int(input())

    while(casos_teste != 0):
        entrada = input()
        valores = entrada.split(' ')

        raio_total = int(valores[0]) + int(valores[1])

        print(raio_total)
        casos_teste -= 1