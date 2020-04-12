# -*- coding: utf-8 -*

entrada = float(input())

if (entrada >= 0) & (entrada <= 25):
    print("Intervalo [0,25]")
elif (entrada > 25) & (entrada <= 50):
    print("Intervalo (25,50]")
elif (entrada > 50) & (entrada <= 75):
    print("Intervalo (50,75]")
elif (entrada > 75) & (entrada <= 100):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")