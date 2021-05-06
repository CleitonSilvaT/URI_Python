# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Entradas
    tipo_cha = int(input())
    entrada = input()
    # Transformando respostas em int
    resposta_participantes = [int(resposta) for resposta in entrada.split(' ')]
    # Identificando total de respostas corretas
    print(resposta_participantes.count(tipo_cha))
