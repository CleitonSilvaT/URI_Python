# -*- coding: utf-8 -*

if __name__ == '__main__':
    # Rodar inumeras vezes
    while(True):
        # Entrada
        x = int(input())
        # Condicao de parada
        if (x == 0):
            break
        # Criar uma string para armazenar a lista
        n = ""
        for i in range(1, x+1):
            # Adicionar numero na lista
            n = n + str(i) + " "
        # Imprimir lista de numeros exceto último elemento (espaco)
        print(n[:-1])