# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entradas
    entrada = input()
    valores = input()
    # Variaveis
    resultado = True
    altura_pulo = entrada.split(' ')[0]
    num_canos = entrada.split(' ')[1]
    altura_canos = valores.split(' ')
    # Iniciando o jogo
    cano_atual = int(altura_canos[0])

    for i in range(1, int(num_canos)):
        # Identificando qual deve ser a altura do pulo
        diferenca = int(altura_canos[i]) - cano_atual
        # Calculando modulo da diferenca para saber se o sapo consegue pular
        if(abs(diferenca) <= int(altura_pulo)):
            cano_atual = int(altura_canos[i])
        # Caso a altura seja muito alta, o sapo nao consegue pular
        else:
            resultado = False
            break

    # Resultado
    if(resultado):
        print('YOU WIN')
    else:
        print('GAME OVER')