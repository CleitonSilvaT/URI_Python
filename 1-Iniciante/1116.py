# -*- coding: utf-8 -*


if __name__ == '__main__':
    # Variaveis
    elementos = []

    # Entrada
    quantidade = int(input())

    while(quantidade > 0):
        par = input()
        elementos.append(par)
        quantidade = quantidade - 1


    for conjunto in elementos:
        valores = conjunto.split(" ")
        x = int(valores[0])
        y = int(valores[1])

        # Verificar divisao por zero
        if ( y == 0):
            print("divisao impossivel")

        else:
            resultado = x / y
            print("%.1f" % resultado)