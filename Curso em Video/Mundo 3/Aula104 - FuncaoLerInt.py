# Aula Funções
# Este programa
# Autor: Eduardo Knop


def leiaInt(n=''):
    while n.isnumeric() is False:
        print(f'{cor["r"]}Erro! Valor Inválido.{cor["l"]}')
        n = input('Digite o Número Inteiro Novamente: ')
    return int(n)


cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

while True:
    num = leiaInt(input('Digite um Número Inteiro: '))
    print(f'Você digitou o Número Inteiro {cor["b"]}{num}{cor["l"]}!')
    op = ' '
    while op not in 'NS':
        op = input('Deseja Continuar? ').upper().strip()[0]
    if op == 'N':
        break
