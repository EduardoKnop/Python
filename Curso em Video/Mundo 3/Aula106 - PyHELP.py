# Aula Funções
# Este programa
# Autor: Eduardo Knop

from time import sleep

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m',
       'p': '\033[1;35m',
       'lb': '\033[1;36m',
       'w': '\033[1;37m'
       }

while True:
    print(f'{cor["p"]}-=' * 15)
    print(f'{"SISTEMA DE AJUDA PYHELP":^30}')
    print(f'{cor["p"]}-={cor["l"]}' * 15)
    op = input('Função ou Biblioteca > ')
    if op.strip().lower() == 'sair':
        break
    else:
        print(f'{cor["lb"]}Acessando Manual', end='', flush=True)
        for i in range(0, 10):
            print(f'{cor["lb"]}.{cor["b"]}', end='', flush=True)
            sleep(0.3)
        print()
        print(help(op))
print(f'{cor["w"]}VOLTE SEMPRE{cor["l"]}')
