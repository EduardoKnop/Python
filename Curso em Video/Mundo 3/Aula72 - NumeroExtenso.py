# Aula Tuplas
# Este programa escreve por entenso um número entre 0 e 20
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

print('\n\n*-* Este programa escreve o número digitado por extenso *-*\n\n')

n = -1
while n not in range(0, 21):
    n = int(input(f'''{cor['b']}Escolha um número entre 0 e 20: '''))
    if n < 0 or n > 20:
        print(f'''{cor['r']}Número Inválido! Tente Novamente''')
    else:
        print(cor['g'] + numeros[n].capitalize())
