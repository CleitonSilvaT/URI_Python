# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    entrada = input()
    while(entrada != '0 0'):
        aumento_xp = int(entrada.split(' ')[0])
        xp_atual = int(entrada.split(' ')[1])
        # Calculando xp no evento
        novo_xp = xp_atual * aumento_xp
        # Resultado
        print(novo_xp)
        # Entrada
        entrada = input()