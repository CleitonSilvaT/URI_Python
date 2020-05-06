# -*- coding: utf-8 -*

def definicao_quadrante(x, y):
    if (x > 0):
        if (y > 0):
            print("primeiro")
        else:
            print("quarto")

    else:
        if (y > 0):
            print("segundo")
        else:
            print("terceiro")


if __name__ == '__main__':

    while(True):
        # Entrada
        entrada = input()
        coordenadas = entrada.split(" ")
        x = int(coordenadas[0])
        y = int(coordenadas[1])

        # Condicao de parada
        if (x == 0 or y == 0):
            break

        definicao_quadrante(x, y)