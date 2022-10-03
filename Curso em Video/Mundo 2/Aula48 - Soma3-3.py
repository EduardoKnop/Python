# Aula Laços de Repetição
# Este programa calcula a soma de números múltiplos de 3 ímpares até 500
# Autor: Eduardo Knop

from time import sleep

cor = {'l': '\033[m',
       'y': '\033[1;33m'
       }
s = 0

print('''\n{}
*-* Este programa calcula a soma de múltiplos de 3 ímpares até 500 *-*
{}\n'''.format(cor['y'], cor['l']))

print('Calculando...')
sleep(1)
for i in range(3, 501, 3):
    if i % 2 == 1:
        s = s + i
print('A soma é: {}'.format(s))
