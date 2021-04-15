# -*- coding: utf-8 -*-

# Nao eh necessario armazenar dados da matriz (trecho de codigo comentado)
if __name__ == '__main__':
    # Entrada
    ordem_matriz = int(input())

    while(ordem_matriz != 0):
        # Contruindo matriz
        # matriz = []
        # Encontrando o ultimo/maior valor da matriz
        maior_valor = (2 ** (ordem_matriz - 1)) ** 2
        total_digitos_maior_valor = len(str(maior_valor))

        for i in range(ordem_matriz):
            # line = []
            for j in range(ordem_matriz):
                if(j == 0):
                    potencia = i

                # line.append(2**potencia)
                # Seguindo padrao de impressao do resultado
                print('{value: >{espaco}}'.format(value=2**potencia, espaco=total_digitos_maior_valor), end='')
                potencia += 1
                # Espacamento entre os elementos da matriz
                if j != ordem_matriz - 1:
                    print(' ', end='')
            # matriz.append(line)
            # Separacao de cada linha da matriz
            print()

        # Entrada
        ordem_matriz = int(input())
        # Separando cada matriz impressa
        print()