# Aula Listas
# Este programa verifica o maior e menor valor de uma lista e suas posições
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }
valores = []

print(f'''\n\n{cor["y"]}*-* Este programa verifica o maior e menor valor de uma lista e suas posições *-*{cor["l"]}\n\n''')

for v in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {v}: ')))

print(f'{cor["b"]}Maior Valor: {max(valores)} - Posição:', end=' ')
for pos, v in enumerate(valores):
    if v == max(valores):
        print(f'{pos}...', end='')

print(f'\nMenor Valor: {min(valores)} - Posição:', end=' ')
for pos, v in enumerate(valores):
    if v == min(valores):
        print(f'{pos}...', end='')
