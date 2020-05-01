# -*- coding: utf-8 -*

# Variaveis
testes = []
sapo = 0
rato = 0
coelho = 0

# Entrada
n = int(input())

while (n > 0):
    testes.append(input())
    n = n - 1

# Identificacao das Cobaias
for caso in testes:
    atual = caso.split(" ")
    # Sapos(S), Ratos(R), Coelhos(C)
    if (str(atual[1]) == "S"):
        sapo = sapo + int(atual[0])
    elif (str(atual[1]) == "R"):
        rato = rato + int(atual[0])
    elif (str(atual[1]) == "C"):
        coelho = coelho + int(atual[0])

# Soma das Cobaias
total = sapo + rato + coelho

# Calcular Porcentagens
if (sapo > 0):
    percentual_sapo = (sapo / total) * 100
else:
    percentual_sapo = 0

if (rato > 0):
    percentual_rato = (rato / total) * 100
else:
    percentual_rato = 0

if (coelho > 0):
    percentual_coelho = (coelho / total) * 100
else:
    percentual_coelho = 0

# Resultado
print("Total:", total, "cobaias")
print("Total de coelhos:", coelho)
print("Total de ratos:", rato)
print("Total de sapos:", sapo)
print("Percentual de coelhos: %.2f" % percentual_coelho, "%")
print("Percentual de ratos: %.2f" % percentual_rato, "%")
print("Percentual de sapos: %.2f" % percentual_sapo, "%")