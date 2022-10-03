# Aula Laços de Repetição
# Este programa informa se um dado número é primo
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'y': '\033[1;33m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'b': '\033[1;34m'
       }
primo = 0

print('''\n{}
*-* Este programa informa se um dado número é primo *-*
{}\n'''.format(cor['y'], cor['l']))

n = int(input('Digite um número: '))
for i in range(1, n + 1):
    if n % i == 0:
        print('{}{} '.format(cor['b'], i), end='')
        primo += 1
    else:
        print('{}{} '.format(cor['l'], i), end='')

if primo == 2:
    print('\n\n{}{} é um número Primo.{}'.format(cor['g'], n, cor['l']))
else:
    print('\n\n{}{} não é um Número Primo.{}'.format(cor['r'], n, cor['l']))
