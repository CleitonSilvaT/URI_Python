# -*- coding: utf-8 -*

if __name__ == '__main__':
    # Entradas
    x = int(input())
    y = int(input())

    # Prevalecer ordem x(menor) e y(maior)
    if (x > y):
        temp = y
        y = x
        x = temp

    # Identificar numeros multiplos com restos definidos
    for i in range(x+1, y):
        if (i % 5 == 2 or i % 5 == 3):
            # Resultado
            print(i)