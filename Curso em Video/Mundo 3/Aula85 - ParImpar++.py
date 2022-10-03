# Aula Listas
# Este programa cria uma lista com números pares e ímpares
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

par = []
impar = []
numeros = [par, impar]

for i in range(1, 8):
    num = int(input(f'Digite o {i}º Valor: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

par.sort()
impar.sort()
print(f'''\nOs valores Pares digitados foram: {cor["b"]}{par}{cor["l"]}
Os valores Ímpares digitados foram: {cor["b"]}{impar}{cor["l"]}''')
