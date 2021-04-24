# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Variavel
    total_aparelhos = 0

    # Entrada
    entrada = input()
    num_tomadas = entrada.split(' ')

    # Encontrando o total de aparelhos que podem ser conectados nas reguas
    for regua in num_tomadas:
        total_aparelhos += int(regua)

    # Conectando as 4 reguas entre si
    total_aparelhos -= 3

    # Resultado
    print(total_aparelhos)