# Aula Laços de Repetição
# Este programa calcula o fatorial de um número
# Autor: Eduardo Knop

fat = 1

num = int(input('Escolha um número para fazer o Fatorial: '))
print('{}! = '.format(num), end='')
if num > 1:
    while num != 0:
        fat = num * fat
        if num > 1:
            print('{} x '.format(num), end='')
        else:
            print('{} = '.format(num), end='')
        num -= 1
print('{}'.format(fat))
