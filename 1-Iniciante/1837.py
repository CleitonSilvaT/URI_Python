# -*- coding: utf-8 -*-

# Conhecer sobre o Teorema da Divisao Euclidiana ou resto da divisao inteira
# Para saber que pode exister ambiguidade ao buscar os valores de resto
# Ao seguir a regra que 0 ≤ r < |b| eh possivel chegar a solucao
if __name__ == '__main__':
    # Entrada
    entrada = input()
    valores = entrada.split(' ')

    a = int(valores[0])
    b = int(valores[1])

    # Computando valores
    r = a % b
    if(r < 0):
        r = r - b
    q = int((a - r) / b)

    # Resultado
    print(str(q), str(r))