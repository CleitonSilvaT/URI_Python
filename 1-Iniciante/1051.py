# -*- coding: utf-8 -*

# 0.00 < 2000.00 - isento
# 2000.01 < 3000.00 - 8 %
# 3000.01 < 4500.00 - 18%
# > 4500.00 - 28%

salario = float(input())

def deducao_renda1(salario):
    salario = salario - 2000.00
    imposto = salario * 8 / 100
    return imposto

def deducao_renda2(salario):
    faixa_anterior = 3000.00
    salario = salario - faixa_anterior
    imposto1 = deducao_renda1(faixa_anterior)
    imposto2 = salario * 18 / 100
    return imposto1 + imposto2

def deducao_renda3(salario):
    faixa_anterior = 4500.00
    salario = salario - faixa_anterior
    imposto1 = deducao_renda2(faixa_anterior)
    imposto2 = salario * 28 / 100
    return imposto1 + imposto2

if (0.00 <= salario <= 2000.00):
    print("Isento")

if (2000.01 <= salario <= 3000.00):
    imposto = deducao_renda1(salario)
    print("R$ %.2f" % imposto)

if (3000.01 <= salario <= 4500.00):
    imposto = deducao_renda2(salario)
    print("R$ %.2f" % imposto)

if (salario > 4500.00):
    imposto = deducao_renda3(salario)
    print("R$ %.2f" % imposto)