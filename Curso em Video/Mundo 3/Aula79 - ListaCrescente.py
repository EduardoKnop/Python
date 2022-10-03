# Aula Listas
# Este programa
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

valores = []

while True:
    valor = int(input('Insira um valor: '))
    if valor in valores:
        print(f'{cor["r"]}Valor já existente! Não adicionado.{cor["l"]}')
    else:
        valores.append(valor)
        print(f'{cor["g"]}{valor} adicionado com sucesso!{cor["l"]}')
    
    op = ' '
    while op not in 'SN':
        op = input('Deseja adicionar outro valor? ').upper().strip()[0]
    if op in 'N':
        break

valores.sort()
print(valores)
