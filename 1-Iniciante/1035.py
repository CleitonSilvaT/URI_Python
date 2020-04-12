# -*- coding: utf-8 -*

entrada = input()

valores = entrada.split(" ")

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
d = int(valores[3])

if (b > c):
    if (d > a):
        if (c + d) > (a + b):
            if (c > 0) & (d > 0):
                if (a % 2 == 0):
                    print("Valores aceitos")
                else:
                    print("Valores nao aceitos")
            else:
                print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")
