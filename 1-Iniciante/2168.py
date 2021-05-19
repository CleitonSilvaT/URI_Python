# -*- coding: utf-8 -*-

# Levando em consideracao todas as dimensoes da quadra, analisar se uma
# Esquina que nao esta iluminada tem como suas vizinhas esquinas que
# Tambem nao estao iluminadas
def consulta_quarteirao(matriz, inicio_i, inicio_j, termino_i,termino_j):
    for i in range(inicio_i, termino_i+1):
        for j in range(inicio_j, termino_j+1):
            if (matriz[i][j] == 0):
                if (i < termino_i and j < termino_j):
                    if (matriz[i + 1][j] == 0 and matriz[i][j + 1] == 0):
                        return False
                if (i > inicio_i and j > inicio_j):
                    if (matriz[i - 1][j] == 0 and matriz[i][j - 1] == 0):
                        return False
                if (i > inicio_i and j < termino_j):
                    if (matriz[i - 1][j] == 0 and matriz[i][j + 1] == 0):
                        return False
                if (i < termino_i and j > inicio_j):
                    if (matriz[i + 1][j] == 0 and matriz[i][j - 1] == 0):
                        return False
    return True

if __name__ == '__main__':
    # Entrada
    quantidade = int(input())
    # Variavel
    matriz = []

    # Criando matriz que represente todas as informacoes das quadras
    for i in range(quantidade + 1):
        line = []
        # Entrada
        valores = input()
        for j in range(quantidade + 1):
            valor = int(valores.split(' ')[j])
            line.append(valor)
        matriz.append(line)

    for i in range(quantidade):
        for j in range(quantidade):
            if(i+1 <= quantidade and j+1 <= quantidade):
                # Identificando quais os valores fazem parte de uma quadra
                inicio_quarteirao_i = i
                inicio_quarteirao_j = j
                termino_quarteirao_i = i + 1
                termino_quarteirao_j = j + 1
                # Identificando se a quadra esta iluminado
                iluminada = consulta_quarteirao(matriz, inicio_quarteirao_i, inicio_quarteirao_j, termino_quarteirao_i, termino_quarteirao_j)
                # Resultado
                if(iluminada == True):
                    print('S', end='')
                else:
                    print('U', end='')
        # Separando as quadras
        print()