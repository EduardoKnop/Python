# Aula Laços de Repetição - Pt 2
# Este programa é um jogo de adivinhação
# Autor: Eduardo Knop

from random import randint
from time import sleep

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       }
c = 1
user = -1

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar!!!')
print('-=-' * 20)
print('\nProcessando...\n')
sleep(1)

n = randint(0, 10)
while user != n:
    user = int(input('Em que número eu pensei? '))
    if user > 10 or user < 0:
        print('Esse número está fora do range especificado.\n')
    elif user != n:
        print('{}Você errou. Tente novamente.{}\n'.format(cor['r'], cor['l']))
        c += 1
print('{}Parabéns!!! Você acertou o número na {}ª tentativa.{}'.format(cor['g'], c, cor['l']))
