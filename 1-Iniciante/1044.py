# -*- coding: utf-8 -*

entrada = input()

valores = entrada.split(" ")

a = int(valores[0])
b = int(valores[1])

if (a % b == 0) or (b % a == 0):
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")