# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    entrada = int(input())
    # Construir duas listas com os principais numeros arabicos/romanos
    # onde cada indice representa o mesmo numero
    arabicos = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    romanos = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    resultado = ''
    # Controlar indice
    max = len(arabicos) - 1

    # Para encontrar a melhor solucao possivel deve sempre procurar
    # o maior valor possivel que represente o numero naquele momento
    while(entrada > 0):
        # Navegando na lista em ordem decrescente
        for i in range(max, -1, -1):
            if(entrada >= arabicos[i]):
                entrada -= arabicos[i]
                resultado += romanos[i]
                break
    # Resultado
    print(resultado)