# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Constantes
    notas = [2, 5, 10, 20, 50, 100]
    # Entrada
    entrada = input()
    # Condicao de parada
    while(entrada != '0 0'):
        valor_compra = int(entrada.split(' ')[0])
        valor_pago = int(entrada.split(' ')[1])
        # Valor do troco
        troco = valor_pago - valor_compra
        # Quantidade de notas para dar o troco
        qt_nota = 0
        # Percorrer a lista de notas (em ordem inversa) e encontrar sempre
        # A maior nota possivel para fornecer o troco
        while(troco > 0):
            for i in range(len(notas)-1, -1, -1):
                if(troco >= notas[i]):
                    troco -= notas[i]
                    qt_nota += 1
                    break
            # Caso nao exista nenhuma nota possivel para atingir o troco
            else:
                break

        # Atendendo a resolucao (quantidade de notas e troco total entregue)
        if(qt_nota == 2 and troco == 0):
            print('possible')
        else:
            print('impossible')
        # Proxima entrada
        entrada = input()