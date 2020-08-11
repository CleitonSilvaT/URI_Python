# -*- coding: utf-8 -*

if __name__ == '__main__':
    # Entrada
    casos_teste = int(input())

    # Capturar os demais valores de entrada
    while(casos_teste > 0):
        # Tratando as entradas
        entrada = input()
        valores = entrada.split(" ")
        populacao_a = int(valores[0])
        populacao_b = int(valores[1])
        crescimento_a = float(valores[2])
        crescimento_b = float(valores[3])

        tempo = 0

        while(populacao_a <= populacao_b):
            # Condicao de parada
            if(tempo >= 100):
                print("Mais de 1 seculo.")
                break

            tempo += 1
            # Identificando quantas pessoas almentam por ano
            taxa_crescimento_a = populacao_a * crescimento_a / 100
            taxa_crescimento_b = populacao_b * crescimento_b / 100

            # Atualizando o valor da populacao
            populacao_a += int(taxa_crescimento_a)
            populacao_b += int(taxa_crescimento_b)

        else:
            # Resultado
            print(str(tempo) + " anos.")

        casos_teste -= 1