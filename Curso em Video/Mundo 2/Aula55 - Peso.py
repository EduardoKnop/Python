# Aula Laços de Repetição
# Este programa lê o peso de 5 pessoas e informa o maior e o menor
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

print('''\n{}
*-* Este programa lê o peso de 5 pessoas e informa o maior e o menor *-*
{}\n'''.format(cor['y'], cor['l']))

maior = float(input('Digite o 1º peso: '))
menor = maior
for i in range(2, 6):
    peso = float(input('Digite o {}º peso: '.format(i)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('{}{} kg foi o maior peso{} e {}{} kg foi o menor{}'.format(cor['b'], maior, cor['l'], cor['g'], menor, cor['l']))
