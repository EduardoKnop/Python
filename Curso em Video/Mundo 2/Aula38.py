# Aula Condições Aninhadas
# Este programa
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

print('\n\n{}*-* Este programa compara valores *-*{}\n\n'.format(cor['y'], cor['l']))

n1 = int(input('Qual o primeiro valor? '))
n2 = int(input('Qual o segundo valor? '))

if n1 > n2:
    print('\nO {0}primeiro valor{1} é {0}maior{1}!'.format(cor['b'], cor['l']))
elif n2 > n1:
    print('\nO {0}segundo valor{1} é {0}maior{1}!'.format(cor['b'], cor['l']))
else:
    print('\nOs dois valores são {}iguais{}!'.format(cor['b'], cor['l']))
