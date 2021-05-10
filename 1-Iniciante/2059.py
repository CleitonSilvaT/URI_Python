# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    entrada = input()
    escolha_j1 = int(entrada.split(' ')[0])
    num_j1 = int(entrada.split(' ')[1])
    num_j2 = int(entrada.split(' ')[2])
    roubo_j1 = int(entrada.split(' ')[3])
    acusacao_j2 = int(entrada.split(' ')[4])

    # Regras do Jogo
    if(roubo_j1 and acusacao_j2):
        print('Jogador 2 ganha!')
    elif(roubo_j1 and (acusacao_j2 == 0)):
        print('Jogador 1 ganha!')
    elif((roubo_j1 == 0) and acusacao_j2):
        print('Jogador 1 ganha!')
    else:
        soma = num_j1 + num_j2
        if(escolha_j1 and (soma % 2 == 0)):
            print('Jogador 1 ganha!')
        elif((escolha_j1 == 0) and (soma % 2 != 0)):
            print('Jogador 1 ganha!')
        else:
            print('Jogador 2 ganha!')