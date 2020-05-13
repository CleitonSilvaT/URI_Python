# -*- coding: utf-8 -*

# Funcao para computar a media de 2 notas
def calcular_media():
    # Variaveis
    notas = []

    while (len(notas) < 2):
        #Entrada das Notas
        valor = float(input())

        # Notas Validas [0,10]
        if (0 <= valor <= 10):
            notas.append(valor)

        else:
            print("nota invalida")

    # Calcular a media de 2 notas
    media = (notas[0] + notas[1]) / len(notas)
    # Resultado
    print("media = %.2f" % media)

# Função para computar a opcao para calcular novamente a media
def novo_calculo():
    while(True):
        # Entrada
        print("novo calculo (1-sim 2-nao)")
        x = int(input())

        if (x == 1):
            calcular_media()

        elif (x == 2):
            break

if __name__ == '__main__':
    # Calcular a media inicial
    calcular_media()
    # Identificar se sera necessario novo calculo
    novo_calculo()