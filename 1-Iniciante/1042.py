# -*- coding: utf-8 -*

entrada = input()

valores = entrada.split(" ")

# Criar uma lista com os elementos como inteiros
inteiros = [int(valores[0]), int(valores[1]), int(valores[2])]

# Copiar vetor
ordenados = inteiros.copy()
# Ordenando novo vetor
ordenados.sort()

# Imprimir lista ordenada
for elemento in ordenados:
    print(elemento)

# Imprimir espaço em branco
print()

# Imprimir lista original
for elemento in inteiros:
    print(elemento)