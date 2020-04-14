# -*- coding: utf-8 -*

entrada1 = input()

numeros = entrada1.split(" ")

n1 = float(numeros[0]) # Peso 2
n2 = float(numeros[1]) # Peso 3
n3 = float(numeros[2]) # Peso 4
n4 = float(numeros[3]) # Peso 1

pesos = 2 + 3 + 4 + 1
notas = (n1*2) + (n2*3) + (n3*4) + (n4*1)
media = notas/pesos

print("Media: %.1f" % media)

if(media >= 7.0):
    print("Aluno aprovado.")
elif (media < 5.0):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")

    exame = float(input())
    print("Nota do exame:", exame)
    total = (media + exame) / 2
    if (total >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final: %.1f" % total)