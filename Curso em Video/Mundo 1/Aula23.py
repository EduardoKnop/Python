# Aula Strings
# Este programa
# Autor: Eduardo Knop

print('\n\n*-* Este programa separa números de 0 a 9999 por unidades *-*\n\n')

num = str(input('Digite um número de 0 a 9999: '))
if len(num) > 4:
    print('Número Inválido')
elif len(num) == 4:
    print('\nMilhar: {:>6} \nCentena: {:>5} \nDezena: {:>6} \nUnidade: {:>5}'.format(num[0], num[1], num[2], num[3]))
elif len(num) == 3:
    print('\nCentena: {:>5} \nDezena: {:>6} \nUnidade: {:>5}'.format(num[0], num[1], num[2]))
elif len(num) == 2:
    print('\nDezena: {:>6} \nUnidade: {:>5}'.format(num[0], num[1]))
else:
    print('\nUnidade: {:>5}'.format(num[0]))
