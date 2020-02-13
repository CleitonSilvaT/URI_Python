# -*- coding: utf-8 -*

notasDisponiveis = [100, 50, 20, 10, 5, 2, 1]

valor = int(input())

print(valor)

# Passar por todas as notas disponíveis
for cedula in notasDisponiveis:
    # Computar a quantidade de notas disponíveis
    quantidade = 0
    # Sempre pegar a maior nota possível
    while valor >= cedula:
        # Atualizar quantidade de notas e novo valor
        quantidade = quantidade + 1
        valor = valor - cedula

    print(quantidade, "nota(s) de R$",str(cedula) + ",00")