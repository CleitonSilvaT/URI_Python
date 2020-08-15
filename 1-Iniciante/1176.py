# -*- coding: utf-8 -*


if __name__ == '__main__':
    # Variaveis
    fibonacci = []
    # Por definicao o valor 0 e 1 da lista devem ser dados
    fibonacci.append(0)
    fibonacci.append(1)

    # Entrada
    casos_teste = int(input())

    while(casos_teste > 0):
        # Entrada
        valor = int(input())

        # Somente serao calculados os valores que ainda nao foram calculados anteriormente
        if(len(fibonacci) - 1 < valor):
            # Calcular e acumular os valores de fibonacci
            for i in range(len(fibonacci), valor+1):
                valor1 = len(fibonacci) - 1
                valor2 = len(fibonacci) - 2
                fibonacci.append(fibonacci[valor1] + fibonacci[valor2])

        # Resultado
        print("Fib(" + str(valor) + ") = "  + str(fibonacci[valor]))

        casos_teste -= 1