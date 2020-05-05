# -*- coding: utf-8 -*

if __name__ == '__main__':

    while(True):
        # Entrada
        entrada = input()

        valores = entrada.split(" ")

        # Atribuindo valores para x e y
        x = int(valores[0])
        y = int(valores[1])

        # Condicao de parada do programa
        if (x == y):
            break

        # Resultados
        elif (x > y):
            print("Decrescente")

        else:
            print("Crescente")