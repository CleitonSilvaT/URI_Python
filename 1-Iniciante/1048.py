# -*- coding: utf-8 -*

salario = float(input())

def computa_salario(salario, percentual):
    reajuste = salario * percentual / 100
    novo_salario = salario + reajuste

    print("Novo salario: %.2f" % novo_salario)
    print("Reajuste ganho: %.2f" % reajuste)
    print("Em percentual:", percentual, "%")


if ( 0 <= salario <= 400.00 ):
    percentual = 15
    computa_salario(salario, percentual)

elif ( 400.01 <= salario <= 800.00 ):
    percentual = 12
    computa_salario(salario, percentual)

elif ( 800.01 <= salario <= 1200.00):
    percentual = 10
    computa_salario(salario, percentual)

elif ( 1200.00 <= salario <= 2000.00):
    percentual = 7
    computa_salario(salario, percentual)

else:
    percentual = 4
    computa_salario(salario, percentual)