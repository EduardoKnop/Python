# Aula Listas
# Este programa gera palpites para a Mega Sena
# Autor: Eduardo Knop

from random import randint
from time import sleep

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

palpites = []

jogos = int(input('Para quantos Jogos você deseja um Palpite? '))
for j in range(0, jogos):
    print(f'{cor["b"]}JOGO {j + 1}: ', end='')
    palpites.append(list())
    for p in range(0, 6):
        palran = randint(1, 60)
        while palran in palpites[j]:
            palran = randint(1, 60)
        palpites[j].append(palran)
    palpites[j].sort()
    print(f'{cor["g"]}{palpites[j]}{cor["l"]}\n', end='')
    sleep(1)
print(f'{cor["y"]}\nBOA SORTE{cor["l"]}')
