# Aula Tuplas
# Este programa cria uma tupla com 5 números aleatórios
# Autor: Eduardo Knop

from random import randint

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

numeros = (randint(0, 100), randint(0, 100), randint(0, 100),
           randint(0, 100), randint(0, 100))

print(f'''\n{cor['y']}
*-* Este programa cria uma tupla com 5 números aleatórios *-*{cor['l']}\n
''')

print(f'''{cor['b']}Tupla Gerada: {cor['y']}{numeros}
{cor['b']}Menor Número: {cor['y']}{sorted(numeros)[0]}
{cor['b']}Maior Número: {cor['y']}{sorted(numeros)[-1]}{cor['l']}''')
