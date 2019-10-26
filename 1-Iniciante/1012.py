# -*- coding: utf-8 -*

info = input().split(' ')
a = float(info[0])
b = float(info[1])
c = float(info[2])
pi = 3.14159

triangulo = (a * c) / 2
circulo = pi * c ** 2
trapezio = (a + b) * c / 2
quadrado = b ** 2
retangulo = a * b

print("TRIANGULO: %.3f" % triangulo)
print("CIRCULO: %.3f" % circulo)
print("TRAPEZIO: %.3f" % trapezio)
print("QUADRADO: %.3f" % quadrado)
print("RETANGULO: %.3f" % retangulo)