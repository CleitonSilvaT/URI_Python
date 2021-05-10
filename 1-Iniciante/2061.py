# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    entrada = input()
    abas_iniciais = int(entrada.split(' ')[0])
    acoes_realizadas = int(entrada.split(' ')[1])
    # Capturando todas as acoes realizadas
    while(acoes_realizadas > 0):
        acao = input()
        if(acao == 'fechou'):
            # Lembrando que ele fecha a aba e abre duas novas
            # Irei somar somente 1 por considerar que nao foi fechado nenhuma aba
            abas_iniciais += 1
        else:
            abas_iniciais -= 1
        acoes_realizadas -= 1
    # Resultado
    print(abas_iniciais)