# Aula Condições
# Este programa indica qual é o menor e maior valor entre um conjunto de 3 números
# Autor: Eduardo Knop

print('\n\n*-* Este programa *-*\n\n')

n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
n3 = float(input('Digite o 3° número: '))

if n1 > n2 > n3:
    print('''Entre {0}, {1} e {2}:
    - {0} é o Maior número
    - {2} é o Menor número'''.format(n1, n2, n3))
elif n1 > n3 > n2:
    print('''Entre {0}, {1} e {2}:
    - {0} é o Maior número
    - {1} é o Menor número'''.format(n1, n2, n3))
elif n2 > n1 > n3:
    print('''Entre {0}, {1} e {2}:
    - {1} é o Maior número
    - {2} é o Menor número'''.format(n1, n2, n3))
elif n2 > n3 > n1:
    print('''Entre {0}, {1} e {2}:
    - {1} é o Maior número
    - {0} é o Menor número'''.format(n1, n2, n3))
elif n3 > n2 > n1:
    print('''Entre {0}, {1} e {2}:
    - {2} é o Maior número
    - {0} é o Menor número'''.format(n1, n2, n3))
else:
    print('''Entre {0}, {1} e {2}:
    - {2} é o Maior número
    - {1} é o Menor número'''.format(n1, n2, n3))
