# Aula Laços de Repetição
# Este programa informa quantas pessoas são de maior em um grupo de 7
# Autor: Eduardo Knop

from datetime import date

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m'
       }
num = 0

print('''\n{}
*-* Este programa informa quantas pessoas são de maior em um grupo de 7 *-*
{}\n'''.format(cor['y'], cor['l']))

ano = date.today().year
print('Você irá informar o ano de nascimento de cada pessoa abaixo: ')
for p in range(0, 7):
    idade = int(input('Informe o ano de nascimento da {}º pessoa: '.format(p + 1)))
    idade = ano - idade
    if idade >= 18:
        num = num + 1

print('''\nNeste grupo há:
{}{} pessoa(s) Maior(es) de Idade \n{}{} pessoa(s) Menor(es) de Idade
{}'''.format(cor['g'], num, cor['r'], 7 - num, cor['l']))
