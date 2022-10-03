# Aula Módulos
# Este programa sorteará um nome entre quatro escolhidos
# Autor: Eduardo Knop

import random

print('\n\nEste programa sorteará um nome entre quatro escolhidos\n\n')

nome1 = input('Digite o 1° nome: ')
nome2 = input('Digite o 2° nome: ')
nome3 = input('Digite o 3° nome: ')
nome4 = input('Digite o 4° nome: ')

nomes = [nome1, nome2, nome3, nome4]

print('\nO aluno escolhido foi {}'.format(random.choice(nomes)))
