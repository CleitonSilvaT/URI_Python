# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    casos_teste = int(input())
    while(casos_teste != 0):
        while(casos_teste > 0):
            # Entrada
            qt_pessoas = int(input())
            # Identificando quantas pessoas ficarao nas pontas
            if((qt_pessoas % 2) == 0):
                pessoas_ponta = 2
            else:
                pessoas_ponta = 1
            # Identificando quantas pessoas nao ficarao nas pontas
            demais_pessoas = qt_pessoas - pessoas_ponta
            # Calculando quantidadade de pedidos realizadas
            # Pessoas na ponta = 1 pedido
            # Pessoas que nao estao na ponta = 2 pedidos
            total_pedidos = pessoas_ponta + (demais_pessoas * 2)
            # Resultado
            print(total_pedidos)

            casos_teste -= 1

        casos_teste = int(input())