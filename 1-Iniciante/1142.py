# -*- coding: utf-8 -*

# Funcao para imprimir elementos na mesma linha
def imprimir(valor):
    print(valor, end=" ")

# Funcao principal
if __name__ == '__main__':
    # Variaveis
    elemento = 1
    # Entrada
    n = int(input())

    # Imprimir a quantidade de linhas
    while(n > 0):
        # Cada linha sera composta por 4 elementos
        for i in range(1, 5):
            # O quarto elemento sempre devera imprimir a palavra chave
            if (elemento % 4 == 0):
                print("PUM")

            else:
                imprimir(elemento)
            # Controlar o valor impresso
            elemento += 1
        # Controlar a quantidade de linhas
        n -= 1