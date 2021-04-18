# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    entrada = input()
    dias = entrada.split(' ')
    dia1 = int(dias[0])
    dia2 = int(dias[1])
    dia3 = int(dias[2])

    # Atendendo as possiveis situacoes
    if(dia1 > dia2):
        if(dia2 <= dia3):
            print(':)')
        elif(dia2 > dia3):
            if((dia1 - dia2) > (dia2 - dia3)):
                print(':)')
            elif((dia1 - dia2) <= (dia2 - dia3)):
                print(':(')
    elif(dia1 < dia2):
        if(dia2 >= dia3):
            print(':(')
        elif(dia2 < dia3):
            if((dia2 - dia1) > (dia3 - dia2)):
                print(':(')
            elif((dia2 - dia1) <= (dia3 - dia2)):
                print(':)')
    elif(dia1 == dia2):
        if(dia2 < dia3):
            print(':)')
        else:
            print(':(')