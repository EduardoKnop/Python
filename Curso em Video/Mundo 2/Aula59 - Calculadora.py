# Aula Laços de Repetição - Pt 2
# Este programa é uma calculadora
# Autor: Eduardo Knop

from time import sleep

menu = 4

while menu != 5:
    if menu == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    elif menu == 1:
        print('{} + {} = {}\n'.format(n1, n2, n1 + n2))
        sleep(2)
    elif menu == 2:
        print('{} X {} = {}\n'.format(n1, n2, n1 * n2))
        sleep(2)
    elif menu == 3:
        if n1 > n2:
            print('Entre {} e {}, o maior é {}\n'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {}, o maior é {}\n'.format(n1, n2, n2))
        else:
            print('Os dois valores digitados são iguais: {}\n'.format(n1))
        sleep(2)
    else:
        print('Opção inválida, tente novamente!\n')
        sleep(0.5)

    print('''Digite: \n[ 1 ] para Somar \n[ 2 ] para Multiplicar
[ 3 ] para Maior \n[ 4 ] para Redigitar os Números \n[ 5 ] para Sair''')
    menu = int(input('Opção: '))

print('Programa Encerrado')
