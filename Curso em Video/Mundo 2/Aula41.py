# Aula Condições Aninhamento
# Este programa organiza atletas em suas categorias
# Autor: Eduardo Knop

from datetime import date

cor = {'l': '\033[m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

print('\n\n{}*-* Este programa organiza atletas em suas categorias *-*\n\n{}'.format(cor['y'], cor['l']))

idade = int(input('Em que ano você nasceu? '))
ano = date.today().year
idade = ano - idade

if idade < 10:
    print('Você está na categoria {}MIRIM{}'.format(cor['b'], cor['l']))
elif 9 < idade < 15:
    print('Você está na categoria {}INFANTIL{}'.format(cor['b'], cor['l']))
elif 14 < idade < 20:
    print('Você está na categoria {}JUNIOR{}'.format(cor['b'], cor['l']))
elif idade == 20:
    print('Você está na categoria {}SÊNIOR{}'.format(cor['b'], cor['l']))
else:
    print('Você está na categoria {}MASTER{}'.format(cor['b'], cor['l']))
