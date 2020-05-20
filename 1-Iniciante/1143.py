# -*- coding: utf-8 -*

# Imprimir valores na mesma linha
def imprimir(valor):
    print(valor, end=" ")

# Funcao principal
if __name__ == '__main__':
    # Variaveis
    elemento = 1
    # Entrada
    n = int(input())

    while(n > 0):
        # Padrao de impressao de elementos por linha
        imprimir(elemento)
        imprimir(elemento**2)
        print(elemento**3)

        # Atualizando valores
        elemento += 1
        n -= 1