# Aula Funções
# Este programa
# Autor: Eduardo Knop


def ficha(j='', g=''):
    if len(j) == 0:
        j = f'{cor["r"]}<desconhecido>'
    if len(g) == 0:
        g = 0
    print(f'{cor["l"]}O jogador {cor["g"]}{j}{cor["l"]} fez ', end='')
    print(f'{cor["b"]}{g}{cor["l"]} gol(s) no campeonato.')


cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

while True:
    ficha(input('Nome do Jogador: '), input('Número de Gols: '))
    op = ' '
    while op not in 'NS':
        op = input('Deseja Continuar? ').strip().upper()[0]
    if op == 'N':
        break
