# Aula Laços de Repetição
# Este programa faz uma contagem regressiva
# Autor: Eduardo Knop

from time import sleep

cor = {'l': '\033[m',
       'b': '\033[1;34m',
       'y': '\033[1;33m'
       }

print('''\n{}
*-* Este programa faz uma contagem regressiva *-*
\n{}'''.format(cor['b'], cor['l']))

print('Iniciando em...')
for i in range(10, -1, -1):
    sleep(1)
    print(i)
    if i == 4:
        print(cor['b'], end='')
print('{}FELIZ ANO NOVO!{}'.format(cor['y'], cor['l']))
