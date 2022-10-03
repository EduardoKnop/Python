# Aula Condições
# Este programa calcula o preço da viagem
# Autor: Eduardo Knop

print('\n\n*-* Este programa *-*\n\n')

km = float(input('Qual a distância até o destino? '))

if km <= 200:
    print('\nO preço por uma viagem de {:.1f} km é de R$ {:.2f}.'.format(km, (km * 0.5)))
else:
    print('\nO preço por uma viagem de {:.1f} km é de R$ {:.2f}.'.format(km, (km * 0.45)))
print('Tenha uma boa viagem!')
