# Aula Funções
# Este programa informa o maior valor de uma lista
# Autor: Eduardo Knop

from time import sleep


def maior(* v):
    print('Analisando os valores passados...', flush=True)
    sleep(1)
    m = 0
    if len(v) == 1:
        m = v[0]
    elif len(v) > 1:
        m = max(v)
    for i in v:
        print(f'{cor["b"]}{i}{cor["l"]}', end=' ', flush=True)
        sleep(0.5)
    sleep(1)
    print(f'''Foram informados {len(v)} valores ao todo.
O maior valor informado foi {m}.''', flush=True)
    sleep(1)
    print('-=' * 15, flush=True)


cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
