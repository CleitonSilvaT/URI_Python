# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Constantes
    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    dias = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while(True):
        # Condicao de parada
        try:
            # Entrada
            data = input()
        except(EOFError):
            break

        mes = int(data.split(' ')[0])
        dia = int(data.split(' ')[1])

        # Tratamentos para o mes 12
        if(mes == 12):
            if(dia == 24):
                print('E vespera de natal!')
            elif(dia == 25):
                print('E natal!')
            elif(dia > 25):
                print('Ja passou!')
            else:
                faltam_dias = 25 - dia
                print('Faltam %d dias para o natal!' % faltam_dias)
        # Tratamento para os demais meses
        else:
            # Ajuste para buscar o mes desejado
            mes = mes - 1
            # Somar a quantidade total de dias, a partir do mes informado
            # Diminuir a quantidade de dias que passaram no mes informado
            # Diminuir a quantidade de dias excedentes do mes 12
            faltam_dias = sum(dias[mes::]) - dia - 6
            print('Faltam %d dias para o natal!' % faltam_dias)