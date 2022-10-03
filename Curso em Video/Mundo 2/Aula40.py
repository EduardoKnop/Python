# Aula Condições Aninhamento
# Este programa indica se um aluno está aprovado, reprovado ou de recuperação
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

print('{}\n\n*-* Este programa calcula a média e a situação do aluno *-*\n\n{}'.format(cor['b'], cor['l']))

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2

if m < 5:
    print('\n{}REPROVADO'.format(cor['r']))
elif m >= 7:
    print('\n{}APROVADO'.format(cor['g']))
else:
    print('\n{}EM RECUPERAÇÃO'.format(cor['y']))
print('{}Média: {:.1f}{}'.format(cor['b'], m, cor['l']))
