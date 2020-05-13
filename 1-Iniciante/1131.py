# -*- coding: utf-8 -*

# Variaveis globais
grenais = 0
vitoria_inter = 0
vitoria_gremio = 0
empates = 0

# Funcao para impimir os resultados computados
def imprimir_resultados():
    # Variaveis
    global grenais
    global vitoria_inter
    global vitoria_gremio
    global empates

    print(grenais, "grenais")
    print("Inter:" + str(vitoria_inter))
    print("Gremio:" + str(vitoria_gremio))
    print("Empates:" + str(empates))

    if (vitoria_inter > vitoria_gremio):
        print("Inter venceu mais")

    elif (vitoria_gremio > vitoria_inter):
        print("Gremio venceu mais")

    else:
        print("Nao houve vencedor")

# Funcao para computar os dados de um grenal
def computa_grenal():
    # Variaveis
    global grenais
    global vitoria_inter
    global vitoria_gremio
    global empates

    # Atualizar numero de grenais
    grenais = grenais + 1

    # Entrada
    valores = input()

    gols = valores.split(" ")
    gols_inter = int(gols[0])
    gols_gremio = int(gols[1])

    # Calcular vitoria
    if (gols_inter > gols_gremio):
        vitoria_inter = vitoria_inter + 1

    elif (gols_gremio > gols_inter):
        vitoria_gremio = vitoria_gremio + 1

    else:
        empates = empates + 1

# Funcao para calcular um novo grenal
def novo_grenal():

    while(True):
        # Entrada
        print("Novo grenal (1-sim 2-nao)")
        valor = int(input())

        if (valor == 1):
            computa_grenal()

        elif(valor == 2):
            break

if __name__ == '__main__':
    # Computar o primeiro grenal
    computa_grenal()
    # Identificar todos os grenais
    novo_grenal()
    # Resultado
    imprimir_resultados()
