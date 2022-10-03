# Aula Listas
# Neste programa 4 jogadores jogam um dado
# Autor: Eduardo Knop

from random import randint
from time import sleep
from operator import itemgetter

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }
res = {'Jogador 1': randint(1, 6),
       'Jogador 2': randint(1, 6),
       'Jogador 3': randint(1, 6),
       'Jogador 4': randint(1, 6)
       }

rank = []

for k, v in res.items():
    print(f'O {k} tirou {v}')
    sleep(1)

rank = sorted(res.items(), key=itemgetter(1), reverse=True)

print('=-' * 13)
for i, j in enumerate(rank):
    print(f'{cor["b"]}{i + 1}º Lugar:{cor["g"]} {j[0]} com {j[1]}{cor["l"]}')
    sleep(1)
