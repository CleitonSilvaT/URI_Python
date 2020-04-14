# -*- coding: utf-8 -*

entrada = input()

valores = entrada.split(" ")

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

def calculaPerimetro():
    perimetro = a + b + c
    print("Perimetro = %.1f" % perimetro)

def calculaArea():
    area = ((a + b) * c) / 2
    print("Area = %.1f" % area)

# Condições de existência de um triângulo
if (a + b) > c:
    if (a + c) > b:
        if (b + c) > a:
            calculaPerimetro()
        else:
            calculaArea()
    else:
        calculaArea()
else:
    calculaArea()