# -*- coding: utf-8 -*

# Variáveis
x = []
no_intervalo = 0
fora_intervalo = 0

# Entrada
n = int(input())
while (n > 0):
    x.append(int(input()))
    n = n - 1

# Verificar se os elemtos da lista
for i in x:
    # No intervalo
    if (10 <= i <= 20):
        no_intervalo = no_intervalo + 1
    # Fora do intervalo
    else:
        fora_intervalo = fora_intervalo + 1

# Resultado
print(no_intervalo, "in")
print(fora_intervalo, "out")