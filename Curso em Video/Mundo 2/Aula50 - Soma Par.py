# Aula Laços de Repetição
# Este programa soma até 6 números pares
# Autor: Eduardo Knop

j = 0
s = [0, 0, 0, 0, 0, 0]

cor = {'l': '\033[m',
       'y': '\033[1;33m'
       }

print('''\n{}
*-* Este programa soma até 6 números se forem pares *-*
{}\n'''.format(cor['y'], cor['l']))

for i in range(0, 6):
    n = int(input('Escreva o {}º Número: '.format(i + 1)))
    if n % 2 == 0:
        s[j] = n
        j += 1

for k in range(0, s.count(0)):
    s.remove(0)

print('\nOs números pares digitados foram: {}'.format(s))
print('E sua soma é {}'.format(sum(s)))
