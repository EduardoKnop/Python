# Aula Condições Aninhadas
# Este programa informa o ano de apresentação no exército
# Autor: Eduardo Knop

from datetime import date

cor = {'l': '\033[m',
       'g': '\033[32m',
       'r': '\033[31m',
       'b': '\033[34m',
       'y': '\033[1;33m'
       }

print('\n\n{}*-* Este programa informa o ano de apresentação no exército *-*{}\n\n'.format(cor['y'], cor['l']))

nasc = int(input('Em que ano você nasceu? '))
ano = int(date.today().year)
idade = ano - nasc

if idade < 18:
    print('\nVocê deve se apresentar daqui {}{} ano(s).{}'.format(cor['b'], 18 - idade, cor['l']))
elif idade > 18:
    print('\nVocê {}já se apresentou{} há {} ano(s).'.format(cor['g'], cor['l'], idade - 18))
else:
    print('\nSe fodeu! Vai ter que se {}apresentar esse ano.{}'.format(cor['r'], cor['l']))
