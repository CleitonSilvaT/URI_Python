# -*- coding: utf-8 -*

vendedor = input()
salarioFixo = float(input())
vendas = float(input())

comissao = vendas * 15 / 100

salario = comissao + salarioFixo

print("TOTAL = R$ %.2f" % salario)