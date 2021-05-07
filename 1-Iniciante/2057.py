# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entrada
    entrada = input()
    hora_saida = int(entrada.split(' ')[0])
    tempo_viagem = int(entrada.split(' ')[1])
    fuso_horario = int(entrada.split(' ')[2])
    # Calculando horario final
    horario_destino = hora_saida + tempo_viagem + fuso_horario
    # Ajustes no horario considerando 24 horas
    if(horario_destino >= 24):
        horario_destino = horario_destino - 24
    elif(horario_destino < 0):
        horario_destino = horario_destino + 24
    # Resultado
    print(horario_destino)