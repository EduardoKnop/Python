# Aula Laços de Repetição
# Este programa verifica se uma frase é Palíndromo
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m'
       }

print('''\n{}
*-* Este programa verifica se uma frase é Palíndromo *-*
{}\n'''.format(cor['y'], cor['l']))

frase = str(input('Digite uma frase ou palavra: ')).strip().replace(' ', '')
frase = frase.lower()

if frase[::-1] != frase[::1]:
    print('{}\nNão é um palindromo!{}'.format(cor['r'], cor['l']))
else:
    print('{}\nÉ um palíndromo{}'.format(cor['g'], cor['l']))
