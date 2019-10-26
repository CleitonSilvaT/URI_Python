# -*- coding: utf-8 -*

info1 = input().split(' ')
codigoPeca1 = int(info1[0])
numeroPecas1 = int(info1[1])
valorUnitario1 = float(info1[2])
total1 = valorUnitario1 * numeroPecas1

info2 = input().split(' ')
codigoPeca2 = int(info2[0])
numeroPecas2 = int(info2[1])
valorUnitario2 = float(info2[2])
total2 = valorUnitario2 * numeroPecas2

total = total1 + total2

print("VALOR A PAGAR: R$ %.2f" % total )