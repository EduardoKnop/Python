# Aula Condições
# Este programa indica se um ano é bissexto
# Autor: Eduardo Knop

from datetime import date

print('\n\n*-* Este programa indica se um ano é bissexto *-*\n\n')

ano = int(input('Qual ano você quer saber se é bissexto? 0 para ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 != 0:
        print('\n{} não é um ano bissexto'.format(ano))
    else:
        print('\n{} é um ano bissexto'.format(ano))
else:
    print('\n{} é um ano bissexto'.format(ano))
