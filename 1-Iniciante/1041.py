# -*- coding: utf-8 -*

entrada = input()

valores = entrada.split(" ")

x = float(valores[0])
y = float(valores[1])

if (x == 0.0):
    if (y == 0.0):
        print("Origem")
    else:
        print("Eixo Y")

elif (y == 0.0):
    print("Eixo X")

elif (x > 0.0):
    if  (y > 0.0):
        print("Q1")
    else:
        print("Q4")
elif (x < 0.0):
    if (y > 0.0):
        print("Q2")
    else:
        print("Q3")