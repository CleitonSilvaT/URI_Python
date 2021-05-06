# -*- coding: utf-8 -*-

# Computar elementos da sequencia, em ordem inversa
def sequencia(num, seq):
    if(num == 0):
        return seq.append(num)
    seq += num * [num]
    return sequencia(num - 1, seq)

if __name__ == '__main__':
    # Variavel
    caso_teste = 1
    while(True):
        # Condicao de parada
        try:
            entrada = int(input())
        except(EOFError):
            break

        lista = []
        sequencia(entrada, lista)

        # Resultado
        if(entrada == 0):
            print('Caso {:d}: {:d} numero'.format(caso_teste, len(lista)))
        else:
            print('Caso {:d}: {:d} numeros'.format(caso_teste, len(lista)))

        # Imprimindo lista no padrao, considerando construcao em ordem inversa
        for i in range(len(lista)-1, -1, -1):
            if(i > 0):
                print(lista[i], end=' ')
            else:
                print(lista[i])
        # Espaco entre entradas
        print()
        caso_teste += 1