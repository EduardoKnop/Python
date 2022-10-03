# Aula Condiçoes
# Este programa informa se três retas podem formar um triângulo
# Autor: Eduardo Knop

print('\n\n*-* Este programa *-*\n\n')

seg1 = float(input('Insira o comprimento do 1° Segmento de Reta: '))
seg2 = float(input('Insira o comprimento do 2° Segmento de Reta: '))
seg3 = float(input('Insira o comprimento do 3° Segmento de Reta: '))

if (seg1 + seg2) > seg3 and (seg1 + seg3) > seg2 and (seg2 + seg3) > seg1:
    print('Segmentos de Reta de comprimento {}, {} e {}\033[1;32m FORMAM \033[mum triângulo'.format(seg1, seg2, seg3))
else:
    print('Segmentos de Reta de comprimento {}, {} e {}\033[1;31m NÃO FORMAM\033[m um triângulo'.format(seg1, seg2, seg3))
