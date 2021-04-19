# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Segundo regra definida (0 ≤ Ti ≤ 20) atribuo um valor maior para iniciar
    num_pessoa = 99
    # Segundo regra definida  (1 ≤ N ≤ 100) defino um valor aleatorio para iniciar
    posicao_pessoa = 0

    # Entrada
    total_pessoas = int(input())
    entrada = input()
    pessoas = entrada.split(' ')

    # Encontrado menor numero na lista
    for pessoa in range(total_pessoas):
        if(num_pessoa > int(pessoas[pessoa])):
            num_pessoa = int(pessoas[pessoa])
            # Considerar que as pessoas sao numeradas a partir de 1
            posicao_pessoa = pessoa + 1

    # Resultado
    print(posicao_pessoa)