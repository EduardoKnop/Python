# Aula Laços de Repetição
# Este programa forma um Progressão Aritmética
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'y': '\033[1;33m'
       }

print('''\n{}
*-* Este programa mostra 10 termos de uma Progressão Aritmética *-*
\n{}'''.format(cor['y'], cor['l']))

n1 = int(input('Escolha o número inicial: '))
p = int(input('Escolha o passo: '))

for i in range(n1, n1 + (10 - 1) * p + 1, p):
    if i < n1 + (9 - 1) * p + 1:
        print(i, end=' → ')
    else:
        print(i)
