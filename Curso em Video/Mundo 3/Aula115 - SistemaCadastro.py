c = {'l': '\033[m',
     'r': '\033[1;31m',
     'g': '\033[1;32m',
     'y': '\033[1;33m',
     'b': '\033[1;34m',
     'p': '\033[1;35m',
     'lb': '\033[1;36m',
     }


def menu():
    print(f'{c["l"]}' + ('-=' * 20))
    print('MENU PRINCIPAL'.center(40))
    print('-' * 40)
    print(f'''{c["b"]}[ 1 ]{c["p"]} Ver Pessoas Cadastradas
{c["b"]}[ 2 ]{c["p"]} Cadastrar Nova Pessoa
{c["b"]}[ 3 ]{c["p"]} Sair do Sistema''')
    while True:
        try:
            print(f'{c["l"]}' + ('-' * 40))
            op = int(input(f'{c["y"]}Sua Opção: {c["b"]}'))
            if 1 <= op <= 3:
                print(f'{c["l"]}' + ('-=' * 20))
                return op
            else:
                print(f'{c["r"]}ERRO! Digite uma Opção Válida{c["l"]}')
        except ValueError:
            print(f'{c["r"]}ERRO! Digite o Número Correspondente ', end='')
            print(f'à Opção Desejada.{c["l"]}')


def newRegister():
    print('NOVO CADASTRO'.center(40))
    print('-' * 40)
    try:
        fileR = open('Cadastro.txt')
        fileW = open('Cadastro.txt', 'a')
    except FileNotFoundError:
        fileW = open('Cadastro.txt', 'w')
        fileW.write(f'{c["b"]}{"NOME":^30}{"IDADE":^11}{c["l"]}\n')
        fileW.close()
        fileW = open('Cadastro.txt', 'a')
        fileR = open('Cadastro.txt')
    print(fileR.read())
    print('-' * 40)
    name = input(f'{c["y"]}Nome: {c["g"]}')
    while True:
        try:
            age = int(input(f'{c["y"]}Idade: {c["g"]}'))
            if age > 0:
                break
        except ValueError:
            print(f'{c["r"]}ERRO! Por favor, Digite um Número Inteiro Válido')
            print(f'{c["l"]}', end='')
    fileW.write(f'{c["lb"]}{name:30}  {age} anos{c["l"]}\n')


def openRegister():
    try:
        fileR = open('Cadastro.txt')
    except OSError:
        print(f'{c["r"]}Arquivo não Encontrado  :({c["l"]}')
    else:
        print(fileR.read())


while True:
    op = menu()
    if op == 1:
        openRegister()
    elif op == 2:
        newRegister()
    else:
        break
print('SAINDO DO SISTEMA'.center(40))
print('-=' * 20)
