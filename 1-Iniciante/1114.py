# -*- coding: utf-8 -*


if __name__ == '__main__':
    # Atribuindo senha correta
    senha_correta = 2002

    while(True):
        # Entrada
        senha = int(input())

        # Condicao de parada do programa
        if (senha == senha_correta):
            print("Acesso Permitido")
            break

        # Impressao padrao
        else:
            print("Senha Invalida")

