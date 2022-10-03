# Aula Módulos
# Este programa sorteará uma ordem entre quatro nomes escolhidos
# Autor: Eduardo Knop

import random

print('\n\nEste programa sorteará uma sequência entre os nomes digitados\n\n')

nome1 = input('Digite o 1° nome: ')
nome2 = input('Digite o 2° nome: ')
nome3 = input('Digite o 3° nome: ')
nome4 = input('Digite o 4° nome: ')
nomes = [nome1, nome2, nome3, nome4]
random.shuffle(nomes)

print('\nA sequência escolhida foi {}'.format(nomes))
