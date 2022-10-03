# Aula Funções
# Este programa
# Autor: Eduardo Knop

from time import sleep


def contador(i, f, p):
    if p < 0:
        p = -p
    elif p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}: ')
    sleep(1)
    if i < f:
        for k in range(i, f + 1, p):
            print(f'{k} ', end='', flush=True)
            sleep(0.5)
    else:
        for k in range(i, f - 1, -p):
            print(f'{k} ', end='', flush=True)
            sleep(0.5)
    print('FIM!', flush=True)
    sleep(1)
    print('-=' * 20, flush=True)


cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

print('EXEMPLOS: ')
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é com você!!!')
while True:
    contador(int(input('Início: ')), int(input('Fim:    ')),
             int(input('Passo:  ')))
    op = ' '
    while op not in 'NS':
        op = input('Deseja continuar? ').strip().upper()[0]
    if op == 'N':
        break
