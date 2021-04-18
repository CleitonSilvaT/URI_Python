# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Variavel
    valor = 0

    while(True):
        # Entrada com condicao de parada
        try:
            entrada = input()
        except(EOFError):
            break

        # Atribuindo valores para todas as possibilidades possiveis
        if(entrada == '--*'):
            valor += 1
        elif(entrada == '-*-'):
            valor += 2
        elif (entrada == '-**'):
            valor += 3
        elif(entrada == '*--'):
            valor += 4
        elif(entrada == '*-*'):
            valor += 5
        elif(entrada == '**-'):
            valor += 6
        elif(entrada == '***'):
            valor += 7

        # Resultado
        elif(entrada == 'caw caw'):
            print(valor)
            valor = 0