# -*- coding: utf-8 -*-

# Nao eh necessario criar a matriz completa (codigo comentado)
# Apenas calcular sobre a linha que esta sendo capturada no momento
if __name__ == '__main__':
    # Variaveis
    linhas = 12
    colunas = 12
    # Quantidade de valores que devem ser somados
    valores = 66
    soma = 0

    # Entrada
    operacao = input()
    
    # Matriz
    # m = []
    for i in range(linhas):
        # Construindo cada linha da matriz
        line = []
        for j in range(colunas):
            # Entrada
            valor = float(input())
            line.append(valor)
            if(i == j):
                # Deve ser somado ate j-1 (funcao range eh exclusivo)
                for k in range(j):
                    soma += line[k]
        # m.append(line)

    # Resultado
    if(operacao == 'S'):
        print('%.1f' % soma)

    elif(operacao == 'M'):
        print('%.1f' % (soma / valores))