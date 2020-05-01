# -*- coding: utf-8 -*

# Variavel
n = 1
posicao = 0

# Entrada
# Atribuir o primeiro elemento como sendo o maior
maior = int(input())
posicao = n
n = n + 1

# Encontrar o maior elemento entre a posicao 2 e 100
while (n <= 100):
    # Entrada
    elemento = int(input())
    if (elemento > maior):
        # Atualizar maior elemento e posicao
        maior = elemento
        posicao = n
    # Atualizar indice
    n = n + 1

# Resultado
print(maior)
print(posicao)