# Aula Condições Aninhadas
# Este program é o jogo Pedra, Papel, Tesoura
# Autor: Eduardo Knop

from random import choice
from time import sleep

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

game = ['Pedra', 'Papel', 'Tesoura']

print('{}{:=^40}'.format(cor['b'], ' PEDRA, PAPEL, TESOURA '))
print('{:^40}{}'.format('Let`s Play', cor['l']))

jog = str(input('Escolha sua Jogada: ')).capitalize().strip()
comp = choice(game)
if jog in game:
    print('PEDRA...')
    sleep(0.5)
    print('PAPEL...')
    sleep(0.5)
    print('TESOURA!')
    sleep(0.5)
    print('\nComputador jogou {}.'.format(comp))
    print('Você jogou {}.\n'.format(jog))
else:
    print('{}Opção Inválida! Tente novamente{}'.format(cor['r'], cor['l']))

if comp == 'Pedra':
    if jog == 'Pedra':
        print('{}EMPATE{}'.format(cor['y'], cor['l']))
        print('Ambos jogaram Pedra')
    elif jog == 'Papel':
        print('{}VITÓRIA{}'.format(cor['g'], cor['l']))
        print('Papel ganha de Pedra')
    elif jog == 'Tesoura':
        print('{}DERROTA{}'.format(cor['r'], cor['l']))
        print('Tesoura perde para Pedra')
elif comp == 'Papel':
    if jog == 'Pedra':
        print('{}DERROTA{}'.format(cor['r'], cor['l']))
        print('Pedra perde para Papel')
    elif jog == 'Papel':
        print('{}EMPATE{}'.format(cor['y'], cor['l']))
        print('Ambos jogaram Papel')
    elif jog == 'Tesoura':
        print('{}VITÓRIA{}'.format(cor['g'], cor['l']))
        print('Tesoura ganha de Papel')
elif comp == 'Tesoura':
    if jog == 'Pedra':
        print('{}VITÓRIA{}'.format(cor['g'], cor['l']))
        print('Pedra ganha de Tesoura')
    elif jog == 'Papel':
        print('{}DERROTA{}'.format(cor['r'], cor['l']))
        print('Papel perde para Tesoura')
    elif jog == 'Tesoura':
        print('{}EMPATE{}'.format(cor['y'], cor['l']))
        print('Ambos jogaram Tesoura')
