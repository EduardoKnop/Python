# Aula Condições Aninhadas
# Este programa informa se é possível e de qual tipo é um triângulo
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'b': '\033[1;34m'
       }

print('\n\n*-* Este programa *-*\n\n')

seg1 = float(input('Insira o comprimento do 1° Segmento de Reta: '))
seg2 = float(input('Insira o comprimento do 2° Segmento de Reta: '))
seg3 = float(input('Insira o comprimento do 3° Segmento de Reta: '))

if (seg1 + seg2) > seg3 and (seg1 + seg3) > seg2 and (seg2 + seg3) > seg1:
    print('\nSegmentos de Reta de comprimento', end=' ')
    print('{}, {} e {} {}FORMAM{} um triângulo'.format(seg1, seg2, seg3, cor['g'], cor['l']), end=' ')
    if seg1 == seg2 == seg3:
        print('{}EQUILÁTERO{}.'.format(cor['b'], cor['l']))
    elif seg1 == seg2 or seg2 == seg3 or seg3 == seg1:
        print('{}ISÓSCELES{}.'.format(cor['b'], cor['l']))
    else:
        print('{}ESCALENO{}.'.format(cor['b'], cor['l']))
else:
    print('Segmentos de Reta de comprimento', end=' ')
    print('{}, {} e {} {}NÃO FORMAM{} um triângulo.'.format(seg1, seg2, seg3, cor['r'], cor['l']))
