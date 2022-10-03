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
sumcol3 = sumpar = 0

for line in range(0, 3):
    for col in range(0, 3):
        matriz[line].append(int(input(f'Valor de [{line + 1}, {col + 1}]: ')))
        if matriz[line][col] % 2 == 0:
            sumpar += matriz[line][col]

print()
for line in range(0, 3):
    print(f'{cor["b"]}\t', end='')
    for col in range(0, 3):
        print(f' {matriz[line][col]:^5} ', end='')
        if col < 2:
            print('|', end='')
        else:
            sumcol3 += matriz[line][col]
    print(cor['l'])

print(f'''A soma dos Valores Pares digitados é: {sumpar}
A soma da 3ª Coluna é: {sumcol3}
O maior valor da 2ª Linha é: {max(matriz[1])}''')
