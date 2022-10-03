# Aula Laços de Repetição
# Este programa mostra os números pares entre 1 e 50
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'y': '\033[1;33m'
       }

print('''\n{}
*-* Este programa mostra os números pares entre 1 e 50 *-*
\n{}'''.format(cor['y'], cor['l']))

print('Entre 1 e 50 há os seguintes números pares: ')
for i in range(2, 51, 2):
    if i < 50:
        print(i, end=', ')
    else:
        print(i)
