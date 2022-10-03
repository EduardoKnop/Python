# Aula Tuplas
# Este programa mostra uma listagem de preços
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Penal', 25,
            'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32,
            'Canetas', 22.3, 'Livro', 34.9)

print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)

for i in range(0, len(listagem), 2):
    print(f'{listagem[i]:.<21}R${listagem[i + 1]:>7.2f}')
print('-' * 30)
