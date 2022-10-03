# Aula Condições
# Este programa aumenta seu salário em porcentagens diferentes
# Autor: Eduardo Knop

print('\n\n*-* Este programa *-*\n\n')

s = float(input('Qual seu salário atual? R$ '))

if s > 1250:
    print('\nSeu novo salário será de R$ {:.2f}'.format(s * 1.1))
else:
    print('\nSeu novo salário será de R$ {:.2f}'.format(s * 1.15))
