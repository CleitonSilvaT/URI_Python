# -*- coding: utf-8 -*-

def regras_jogo(pessoa1, pessoa2):
    if (pessoa1 == pessoa2):
        return 'empate'

    elif(pessoa1 == 'tesoura'):
        if((pessoa2 == 'papel') or (pessoa2 == 'lagarto')):
            return pessoa1
        else:
            return pessoa2
    elif(pessoa1 == 'papel'):
        if((pessoa2 == 'pedra') or (pessoa2 == 'Spock')):
            return pessoa1
        else:
            return pessoa2
    elif(pessoa1 == 'pedra'):
        if((pessoa2 == 'lagarto') or (pessoa2 == 'tesoura')):
            return pessoa1
        else:
            return pessoa2
    elif(pessoa1 == 'lagarto'):
        if((pessoa2 == 'Spock') or (pessoa2 == 'papel')):
            return pessoa1
        else:
            return pessoa2
    elif(pessoa1 == 'Spock'):
        if((pessoa2 == 'tesoura') or (pessoa2 == 'pedra')):
            return pessoa1
        else:
            return pessoa2

if __name__ == '__main__':
    # Entrada
    entrada = int(input())

    for i in range(1, entrada + 1):
        # Entrada
        valores = input()
        pessoas = valores.split(' ')

        # Encontrar vencedor de acordo com as regras do jogo
        vencedor = regras_jogo(pessoas[0], pessoas[1])

        # Considerar:
        # pessoas[0] sendo Sheldon
        # pessoas[1] sendo Raj

        # Resultado
        if(vencedor == pessoas[0]):
            print('Caso #' + str(i) + ': Bazinga!')
        elif(vencedor == pessoas[1]):
            print('Caso #' + str(i) + ': Raj trapaceou!')
        elif (vencedor == 'empate'):
            print('Caso #' + str(i) + ': De novo!')