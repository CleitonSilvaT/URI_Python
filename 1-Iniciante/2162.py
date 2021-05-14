# -*- coding: utf-8 -*-

if __name__ == '__main__':
    num_medidas = int(input())
    info = input()
    medida = [int(i) for i in info.split(' ')]
    # Caso em que existem 2 medidas
    if(num_medidas < 3):
        if(medida[0] != medida[1]):
            result = 1
        else:
            result = 0
    # Demais casos
    else:
        for i in range(1, num_medidas-1):
            # Encontrando padrao vale-pico-vale ...
            if(medida[i-1] < medida[i] > medida[i+1]):
                result = 1
            # Contrando padrao pico-vale-pico ...
            elif(medida[i-1] > medida[i] < medida[i+1]):
                result = 1
            # Encontrando casos em que nao existe padrao desejado
            else:
                result = 0
                break
    # Resultado
    print(result)