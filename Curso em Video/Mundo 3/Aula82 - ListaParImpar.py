# Aula Listas
# Este programa gera uma lista par e outra impar a partir de uma uma lista
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

valores = []
par = []
impar = []

while True:
    valores.append(int(input('Digite um Número: ')))
    op = ' '
    while op not in 'NS':
        op = input('Deseja Continuar? ').upper().strip()[0]
    if op == 'N':
        break

for v in valores:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print(f'''\n{cor["y"]}Lista Completa: {valores}
{cor["b"]}Lista de Pares: {par}
{cor["y"]}Lista de Impares: {impar}{cor["l"]}''')
