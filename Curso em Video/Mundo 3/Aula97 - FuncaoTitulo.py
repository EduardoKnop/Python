# Aula Funções
# Este programa escreve a mensagem entre separadores
# Autor: Eduardo Knop

def escreva(txt):
    print('~' * (len(txt) + 2))
    print(f' {txt} ')
    print('~' * (len(txt) + 2))


cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

while True:
    escreva(input('Mensagem: ').strip())
    op = ' '
    while op not in 'NS':
        op = input('Deseja escrever outra mensagem? ').strip().upper()[0]
    if op == 'N':
        break
