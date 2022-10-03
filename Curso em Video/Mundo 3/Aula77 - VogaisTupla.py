# Aula Tuplas
# Este programa mostra as vogais das palavras
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

palavras = ('programar', 'python', 'curso', 'tuplas', 'listas', 'dicionarios',
            'computador', 'software', 'codificar', 'aprender')

for i in range(0, len(palavras)):
    print('\n', palavras[i], end=': ')
    for j in range(0, len(palavras[i])):
        if palavras[i][j] == 'a':
            print('a', end=' ')
        if palavras[i][j] == 'e':
            print('e', end=' ')
        if palavras[i][j] == 'i':
            print('i', end=' ')
        if palavras[i][j] == 'o':
            print('o', end=' ')
        if palavras[i][j] == 'u':
            print('u', end=' ')
