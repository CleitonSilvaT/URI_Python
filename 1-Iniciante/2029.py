# -*- coding: utf-8 -*-

if __name__ == '__main__':
    while(True):
        # Constante
        n = 3.14
        # Condicao de parada
        try:
            # Entrada
            volume = float(input())
            diametro = float(input())
        except(EOFError):
            break
        # Formula para calcular raio
        raio = diametro / 2

        # Derivando formula de calcular volume - volume = n * (raio ** 2) * altura
        altura = volume / (n * (raio ** 2))
        print('ALTURA = %.2f' % altura)
        # Formula para calcular area da base de um cilindro
        area_base = n * (raio ** 2)
        print('AREA = %.2f' % area_base)
