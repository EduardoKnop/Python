# Aula Tuplas
# Este programa
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

valores = (int(input('Informe o 1º Valor: ')),
           int(input('Informe o 2º Valor: ')),
           int(input('Informe o 3º Valor: ')),
           int(input('Informe o 4º Valor: ')))

print(f'Número de vezes que apareceu 9: {valores.count(9)}')

if 3 in valores:
    print(f'Posição do 1º número 3 digitado: {valores.index(3) + 1}')
else:
    print('Não foi digitado o número 3')

print('Valores Pares: ', end='')
for i in range(0, 4):
    if valores[i] % 2 == 0:
        print(valores[i], end=' ')
