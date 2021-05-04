# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Variaveis
    maior_nota = 0
    matricula = 0
    # Entrada
    num_alunos = int(input())

    while(num_alunos > 0):
        info = input().split(' ')
        # Encontrando a maior nota
        if(float(info[1]) > maior_nota):
            maior_nota = float(info[1])
            matricula = int(info[0])
        num_alunos -= 1
    # A maior nota deve ser maior ou igual a 8
    if(maior_nota >= 8):
        print(matricula)
    else:
        print('Minimum note not reached')