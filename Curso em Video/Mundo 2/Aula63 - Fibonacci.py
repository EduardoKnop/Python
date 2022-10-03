# Aula Laços de Repetição
# Este programa mostra a sequência de Fibonacci
# Autor: Eduardo Knop

nv = int(input('Digite a quantidade de números da sequência de Fibonacci: '))
n1 = 0
n2 = 1

if nv == 1:
    print('0')
elif nv == 2:
    print('0 → 1')
elif nv > 2:
    print('0 → 1', end=' → ')
    while nv > 2:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        if nv > 3:
            print(n3, end=' → ')
        else:
            print(n3)
        nv -= 1
else:
    print('Número Inválido')
