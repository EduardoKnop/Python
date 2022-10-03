# Aula Listas
# Este programa preenche uma matriz 3x3
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

matriz = [[], [], []]

for line in range(0, 3):
    for col in range(0, 3):
        matriz[line].append(int(input(f'Digite o Valor de [{line + 1}, {col + 1}]: ')))

print()
for n in range(0, 3):
    print(f'\t  {matriz[n][0]:^4} | {matriz[n][1]:^4} | {matriz[n][2]:^4}')
    if n < 2:
        print('\t', '-' * 20)
print()
