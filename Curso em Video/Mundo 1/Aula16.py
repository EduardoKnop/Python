# Aula Módulos
# Este programa mostra a parte inteira de um número
# Autor: Eduardo Knop

import math

print('\n\n*-* Este programa mostra a parte inteira de um número *-*\n\n')
num = float(input('Digite um número qualquer: '))
print('A parte inteira de {} é {}'.format(num, math.trunc(num)))
