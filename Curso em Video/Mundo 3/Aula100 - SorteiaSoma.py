# Aula Funções
# Este programa sorteia 5 valores e soma os pares
# Autor: Eduardo Knop

from random import randint
from time import sleep


def sorteia(v):
    for i in range(0, 5):
        v.append(randint(1, 10))
    print('Foram sorteados os valores: ', end='', flush=True)
    for i in v:
        print(f'{cor["b"]}{i}{cor["l"]} ', end='', flush=True)
        sleep(0.5)
    print('PRONTO!', flush=True)
    return v


def somaPar(v):
    p = 0
    for i in v:
        if i % 2 == 0:
            p += i
    print(f'Somando os valores pares de {v}, temos {p}')
    return p


cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }
valores = []

valores = sorteia(valores)
somaPar(valores)
