# -*- coding: utf-8 -*-

if __name__ == '__main__':
    while(True):
        try:
            # Entrada
            numero = int(input())
            # Formula para descobrir a senha
            senha = numero - 1
            print(senha)
        except(EOFError):
            break