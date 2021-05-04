# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    num_estrelas = int(input())
    entrada = input()
    valores = entrada.split(' ')
    # Transformando elementos em inteiros
    estrelas = [int(elemento) for elemento in valores]
    # Controlar estrelas que foram atacadas
    estrelas_atacadas = [False for i in estrelas]

    # Variaveis
    i = 0
    total_atacadas = 0

    while(0 <= i < num_estrelas):
        # Identificando casos impar
        if(estrelas[i] % 2 != 0):
            if (estrelas[i] > 0):
                # Pegando carneiro
                estrelas[i] = estrelas[i] - 1
                # Controlando numero de estrelas atacadas
                if(estrelas_atacadas[i] == False):
                    total_atacadas += 1
                    estrelas_atacadas[i] = True
            # Caminhando para a proxima estrela
            i += 1

        # Identificando casos par
        else:
            if (estrelas[i] > 0):
                # Pegando carneiro
                estrelas[i] = estrelas[i] - 1
                # Controlando numero de estrelas atacadas
                if(estrelas_atacadas[i] == False):
                    total_atacadas += 1
                    estrelas_atacadas[i] = True
            # Caminhando para a proxima estrela
            i -= 1
    # Resultado
    print(total_atacadas, sum(estrelas))