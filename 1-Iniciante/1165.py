# -*- coding: utf-8 -*

if __name__ == '__main__':
    # Entrada
    casos_teste = int(input())

    while(casos_teste > 0):
        # Entrada
        numero = int(input())
        # Assumo que todos os numeros sao primos
        primo = True

        # Caso o numero nao seja primo, eu atualizo
        for i in range(2, numero):
            if(numero % i == 0):
                primo = False
                break

        # Resultado
        if(primo):
            print(str(numero), "eh primo")
        else:
            print(str(numero), "nao eh primo")

        casos_teste -= 1