# -*- coding: utf-8 -*

# Receber o valor inteiro com o número de dias
dias = int(input())

anos = 0
meses = 0

# Converter o valor recebido em anos - meses - dias

# O ano tem 365 dias
while dias >= 365:
    anos = int(dias / 365)
    dias = dias - (anos * 365)

# O mês possui 30 dias
while dias >= 30:
    meses = int(dias / 30)
    dias = dias - (meses * 30)

print(anos,"ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")