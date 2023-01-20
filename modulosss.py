import sqlite3
banco = sqlite3.connect('Hospedes.db')
cursor = banco.cursor()

def menu():
    list = ['Cadastar reserva',
            'Lista de quartos ocupados',
            'Remover reserva',
            'Quartos desponiveis'
    ]
    titulo('Menu')
    for v in range(len(list)):
        print(f'{v + 1}: \033[1;34m{list[v]}\033[m')
    linhas()

def titulo(ti):
    print(f'=========== {ti} ====================================================')



def linhas():
    print('=======================================================================')



def cadastrar():
    #cursor.execute("CREATE TABLE pessoas (Nome text, Quarto integer, Tele integer)")

    print('Nome completo: ')
    nome = str(input('>> '))

    print('Numero do quarto: ')
    quarto = str(input('>> '))

    print('CPF: ')
    cpf = str(input('>> '))
    try:
        cursor.execute("INSERT INTO clientes VALUES ('"+nome+"', "+str(quarto)+", "+str(cpf)+") ")
        banco.commit()
    except:
        print('Erro no banco de dados')


def pessoas_cadastradas():
    try:
        cursor.execute("SELECT * FROM clientes")
        list = cursor.fetchall()
        titulo('Hospedes')
        for v in range(len(list)):
            print(f'Nome: {list[v][0]}, Quarto: {list[v][1]}, CPF: {list[v][2]}')
            linhas()
    except:
        print('Erro na lista de cadastrado')


def fechar():
    try:
        print('CPF:')
        cp = str(input('>> '))
        cl = cursor.execute("SELECT * FROM clientes WHERE CPF = '"+cp+"' ")
        for v in cl:
            print(v)
        print('Digite [s] para comfirmar')
        co = str(input('>> ')).upper()

        if co == 'S':
            cursor.execute("DELETE FROM clientes WHERE CPF = '"+cp+"' ")
            banco.commit()
            print('Quarto liberado!')
        else:
            print('Fechamento cancelado!')
        input()
    except:
        print('Erro no fechamento do quarto')


def disponiveis():
    list = [
            110, 115, 120, 125, 150,
            200, 250, 300, 350, 400,
            450, 500, 550, 570, 610,
            640, 690, 760, 803, 900
    ]
    titulo('Quartos disponiveis')
    for v in list:
        print(v)
    linhas()


    