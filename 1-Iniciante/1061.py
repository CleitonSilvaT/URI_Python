# -*- coding: utf-8 -*

entrada1 = input()
entrada2 = input()
entrada3 = input()
entrada4 = input()

valor1 = entrada1.split(" ")
valor2 = entrada2.split(":")
valor3 = entrada3.split(" ")
valor4 = entrada4.split(":")

dia_inicio = int(valor1[1])
hora_inicio = int(valor2[0])
minuto_inicio = int(valor2[1])
segundo_inicio = int(valor2[2])
dia_termino = int(valor3[1])
hora_termino = int(valor4[0])
minuto_termino = int(valor4[1])
segundo_termino = int(valor4[2])


def computa_virada(tempo, inicio, termino):
    return tempo - inicio + termino

def computa_termino_maior(inicio, termino):
    return termino - inicio

if __name__ == '__main__':
    if (dia_inicio == dia_termino):
        dia_gasto = 0

        if (hora_inicio == hora_termino):
            hora_gasto = 0

            if (minuto_inicio == minuto_termino):
                minuto_gasto = 0

                if (segundo_inicio == segundo_termino):
                    segundo_gasto = 0

                elif (segundo_inicio < segundo_termino):
                    segundo_gasto = computa_termino_maior(segundo_inicio, segundo_termino)

            elif (minuto_inicio < minuto_termino):
                minuto_gasto = computa_termino_maior(minuto_inicio, minuto_termino)

                if (segundo_inicio == segundo_termino):
                    segundo_gasto = 0

                elif (segundo_inicio < segundo_termino):
                    segundo_gasto = computa_termino_maior(segundo_inicio, segundo_termino)

                elif (segundo_inicio > segundo_termino):
                    segundo_gasto = computa_virada(60, segundo_inicio, segundo_termino)
                    minuto_gasto = minuto_gasto - 1

        elif (hora_inicio < hora_termino):
            hora_gasto = computa_termino_maior(hora_inicio, hora_termino)

            if (minuto_inicio == minuto_termino):
                minuto_gasto = 0

                if (segundo_inicio == segundo_termino):
                    segundo_gasto = 0

                elif (segundo_inicio < segundo_termino):
                    segundo_gasto = computa_termino_maior(segundo_inicio, segundo_termino)

            elif (minuto_inicio < minuto_termino):
                minuto_gasto = computa_termino_maior(minuto_inicio, minuto_termino)

                if (segundo_inicio == segundo_termino):
                    segundo_gasto = 0

                elif (segundo_inicio < segundo_termino):
                    segundo_gasto = computa_termino_maior(segundo_inicio, segundo_termino)

                elif (segundo_inicio > segundo_termino):
                    segundo_gasto = computa_virada(60, segundo_inicio, segundo_termino)
                    minuto_gasto = minuto_gasto - 1


            elif (minuto_inicio > minuto_termino):
                minuto_gasto = computa_virada(60, minuto_inicio, minuto_termino)
                hora_gasto = hora_gasto - 1

                if (segundo_inicio == segundo_termino):
                    segundo_gasto = 0

                elif (segundo_inicio < segundo_termino):
                    segundo_gasto = computa_termino_maior(segundo_inicio, segundo_termino)

                elif (segundo_inicio > segundo_termino):
                    segundo_gasto = computa_virada(60, segundo_inicio, segundo_termino)
                    minuto_gasto = minuto_gasto - 1

    elif (dia_inicio < dia_termino):
        dia_gasto = computa_termino_maior(dia_inicio, dia_termino)

        if (hora_inicio == hora_termino):
            hora_gasto = 0

            if (minuto_inicio == minuto_termino):
                minuto_gasto = 0

                if (segundo_inicio == segundo_termino):
                    segundo_gasto = 0

                elif (segundo_inicio < segundo_termino):
                    segundo_gasto = computa_termino_maior(segundo_inicio, segundo_termino)

            elif (minuto_inicio < minuto_termino):
                minuto_gasto = computa_termino_maior(minuto_inicio, minuto_termino)

                if (segundo_inicio == segundo_termino):
                    segundo_gasto = 0

                elif (segundo_inicio < segundo_termino):
                    segundo_gasto = computa_termino_maior(segundo_inicio, segundo_termino)

                elif (segundo_inicio > segundo_termino):
                    segundo_gasto = computa_virada(60, segundo_inicio, segundo_termino)
                    minuto_gasto = minuto_gasto - 1

        elif (hora_inicio < hora_termino):
            hora_gasto = computa_termino_maior(hora_inicio, hora_termino)

            if (minuto_inicio == minuto_termino):
                minuto_gasto = 0

                if (segundo_inicio == segundo_termino):
                    segundo_gasto = 0

                elif (segundo_inicio < segundo_termino):
                    segundo_gasto = computa_termino_maior(segundo_inicio, segundo_termino)

            elif (minuto_inicio < minuto_termino):
                minuto_gasto = computa_termino_maior(minuto_inicio, minuto_termino)

                if (segundo_inicio == segundo_termino):
                    segundo_gasto = 0

                elif (segundo_inicio < segundo_termino):
                    segundo_gasto = computa_termino_maior(segundo_inicio, segundo_termino)

                elif (segundo_inicio > segundo_termino):
                    segundo_gasto = computa_virada(60, segundo_inicio, segundo_termino)
                    minuto_gasto = minuto_gasto - 1


            elif (minuto_inicio > minuto_termino):
                minuto_gasto = computa_virada(60, minuto_inicio, minuto_termino)
                hora_gasto = hora_gasto - 1

                if (segundo_inicio == segundo_termino):
                    segundo_gasto = 0

                elif (segundo_inicio < segundo_termino):
                    segundo_gasto = computa_termino_maior(segundo_inicio, segundo_termino)

                elif (segundo_inicio > segundo_termino):
                    segundo_gasto = computa_virada(60, segundo_inicio, segundo_termino)
                    minuto_gasto = minuto_gasto - 1

        elif (hora_inicio > hora_termino):
            dia_gasto = dia_gasto - 1
            hora_gasto = computa_virada(24, hora_inicio, hora_termino)

            if (minuto_inicio == minuto_termino):
                minuto_gasto = 0

                if (segundo_inicio == segundo_termino):
                    segundo_gasto = 0

                elif (segundo_inicio < segundo_termino):
                    segundo_gasto = computa_termino_maior(segundo_inicio, segundo_termino)

            elif (minuto_inicio < minuto_termino):
                minuto_gasto = computa_termino_maior(minuto_inicio, minuto_termino)

                if (segundo_inicio == segundo_termino):
                    segundo_gasto = 0

                elif (segundo_inicio < segundo_termino):
                    segundo_gasto = computa_termino_maior(segundo_inicio, segundo_termino)

                elif (segundo_inicio > segundo_termino):
                    segundo_gasto = computa_virada(60, segundo_inicio, segundo_termino)
                    minuto_gasto = minuto_gasto - 1


            elif (minuto_inicio > minuto_termino):
                minuto_gasto = computa_virada(60, minuto_inicio, minuto_termino)
                hora_gasto = hora_gasto - 1

                if (segundo_inicio == segundo_termino):
                    segundo_gasto = 0

                elif (segundo_inicio < segundo_termino):
                    segundo_gasto = computa_termino_maior(segundo_inicio, segundo_termino)

                elif (segundo_inicio > segundo_termino):
                    segundo_gasto = computa_virada(60, segundo_inicio, segundo_termino)
                    minuto_gasto = minuto_gasto - 1


    print(dia_gasto, "dia(s)")
    print(hora_gasto, "hora(s)")
    print(minuto_gasto, "minuto(s)")
    print(segundo_gasto, "segundo(s)")