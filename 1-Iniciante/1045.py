# -*- coding: utf-8 -*

entrada = input()

valores = entrada.split(" ")

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

lista = [a, b, c]

# Ordeno a lista (Ordem crecente)
lista.sort()
# Inverto a lista (Ordem decrescente)
lista.reverse()

a = lista[0]
b = lista[1]
c = lista[2]

if a >= (b + c):
    print("NAO FORMA TRIANGULO")

else:
    if (a ** 2) == (b ** 2) + (c ** 2):
        print("TRIANGULO RETANGULO")

    else:
        if (a ** 2) > (b ** 2) + (c ** 2):
            print("TRIANGULO OBTUSANGULO")

        if (a ** 2) < (b ** 2) + (c ** 2):
            print("TRIANGULO ACUTANGULO")


    if a == b == c:
        print("TRIANGULO EQUILATERO")

    else:
        if (a == b) or (a == c) or (b == c):
            print("TRIANGULO ISOSCELES")