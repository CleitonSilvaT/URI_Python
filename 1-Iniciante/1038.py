# -*- coding: utf-8 -*

# Como o foco somente é voltado para parte dos valores, podemos criar um DICT com apenas duas chaves:
# CODIGO - PREÇO
tabela = {
    1 : 4.00, # Cachorro Quente
    2 : 4.50, #X-Salada
    3 : 5.00, # X-Bacon
    4 : 2.00, # Torrada Simples
    5 : 1.50 # Refrigerante
}

entrada = input()

valores = entrada.split(" ")

codigo = int(valores[0])
quantidade = int(valores[1])

total = tabela[codigo] * quantidade

print("Total: R$ %.2f" % total)