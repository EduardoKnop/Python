# Aula Condições Aninhadas
# Este programa converte um número de decimal para binário, octal ou hex
# Autor: Eduardo Knop

cor = {'limpa': '\033[m',
       'red': '\033[31m',
       'green': '\033[32m',
       'blue': '\033[1;34m'
       }

print('\n\n{}*-* Este programa faz a conversão de bases numéricas *-*{}\n\n'.format('\033[1;33m', cor['limpa']))

dec = int(input('Qual número em decimal você quer converter? '))
print('''\nDigite:
[ 2 ] para Binário
[ 8 ] para Octal
[ 16 ] para Hexadecimal''')
base = int(input('Para qual base numérica? '))

if base == 2:
    bin = str(bin(dec)).replace('0b', '')
    print('\n{2}{0}{3} em Binário: {2}{1}{3}'.format(dec, bin, cor['blue'], cor['limpa']))
elif base == 8:
    oct = str(oct(dec)).replace('0o', '')
    print('\n{2}{0}{3} em Octal: {2}{1}{3}'.format(dec, oct, cor['blue'], cor['limpa']))
elif base == 16:
    hex = str(hex(dec)).replace('0x', '')
    print('\n{2}{0}{3} em Hexadecimal: {2}{1}{3}'.format(dec, hex, cor['blue'], cor['limpa']))
else:
    print('\n{}Base Inválida!!!{}'.format(cor['red'], cor['limpa']))
