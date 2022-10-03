# Aula Condições
# Este programa informa se um número é par ou ímpar
# Autor: Eduardo Knop

print('\n\n*-* Este programa *-*-\n\n')

n = float(input('Digite um número inteiro: '))

if n % 2 == 0:
    print('\n{:.0f} é um número par'.format(n))
elif n % 2 == 1:
    print('\n{:.0f} é um número ímpar'.format(n))
else:
    print('\nNúmero inválido!!!')
