# Aula Condições
# Este programa é um jogo de adivinhação
# Autor: Eduardo Knop

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!!!')
print('-=-' * 20)

print('\nProcessando...\n')
sleep(2)

n = randint(0, 5)
user = int(input('Em que número eu pensei? '))

if n == user:
    print('\nParabéns!!! Você acertou o número.')
elif user > 5 or user < 0:
    print('\nEsse número está fora do range especificado')
else:
    print('\nVocê errou. O número era {}.'.format(n))
