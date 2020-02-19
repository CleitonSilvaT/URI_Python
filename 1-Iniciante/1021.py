# -*- coding: utf-8 -*
# Capturar o valor de entrada
numero = input()

# Separar os valores
valor = numero.split(".")
notas = int(valor[0])
montar_centavos = "0." + valor[1]
centavos = float(montar_centavos)

notas_disponiveis = [100, 50, 20, 10, 5, 2]
centavos_disponiveis = [0.50, 0.25, 0.10, 0.05, 0.01]


# Função para calcular a quantidade de cada nota que será utilizada
def consulta_notas(nota_atual):
    global notas
    usar = 0
    while notas >= nota_atual:
        usar = usar + 1
        notas = notas - nota_atual

    return usar


# Função para calcular a quantidade de cada moeda que será utilizada
def consulta_moedas(moeda_atual):
    global centavos
    usar = 0

    while centavos >= moeda_atual:
        usar = usar + 1
        # Utilizar round para arredondar para 2 casas decimais
        centavos = round(centavos - moeda_atual, 2)

    return usar


print("NOTAS:")
for nota in notas_disponiveis:
    utilizar_notas = consulta_notas(nota)
    print(utilizar_notas, "nota(s) de R$", str(nota) + ".00")

print("MOEDAS:")
# Somente será usada a moeda de R$1.00 caso as notas que foram utilizadas não conseguiram ser uzadas
if notas == 1:
    print("1 moeda(s) de R$ 1.00")
    notas = notas - 1
else:
    print("0 moeda(s) de R$ 1.00")

for centavo in centavos_disponiveis:
    utilizar_moedas = consulta_moedas(centavo)
    print(utilizar_moedas, "moeda(s) de R$ %.2f" % centavo)
