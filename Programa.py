from modulosss import menu, cadastrar, pessoas_cadastradas, fechar, disponiveis, titulo
import os
while True:
    menu()
    try:
        op = int(input('>> '))

        if op == 1:
            titulo('Resevar quarto')
            cadastrar()
            input('>> ')
            os.system('cls')

        elif op == 2:
            pessoas_cadastradas()
            input('>> ')
            os.system('cls')

        elif op == 3:
            titulo('Remover reserva')
            fechar()
            input('>> ')
            os.system('cls')

        elif op == 4:
            disponiveis()
            input('>> ')
            os.system('cls')

        os.system('cls')
    except:
        print('comando invalido')