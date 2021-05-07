# -*- coding: utf-8 -*-

def regras_jogo(jog_1, jog_2):
    if(jog_1 == 'ataque' and jog_2 == 'ataque'):
        print('Aniquilacao mutua')
    elif(jog_1 == 'pedra' and jog_2 == 'pedra'):
        print('Sem ganhador')
    elif(jog_1 == 'papel' and jog_2 == 'papel'):
        print('Ambos venceram')
    elif(jog_1 == 'ataque'):
        print('Jogador 1 venceu')
    elif(jog_2 == 'ataque'):
        print('Jogador 2 venceu')
    elif(jog_1 == 'pedra'):
        print('Jogador 1 venceu')
    elif(jog_2 == 'pedra'):
        print('Jogador 2 venceu')

if __name__ == '__main__':
    # Entrada
    casos_teste = int(input())

    while(casos_teste > 0):
        # Entrada
        jogador_1 = input()
        jogador_2 = input()
        # Encontrando vencedor
        regras_jogo(jogador_1, jogador_2)
        casos_teste -= 1