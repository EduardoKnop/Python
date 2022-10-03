# Aula Laços de Repetição Pt2
# Este programa faz a Progressão Aritmética de um dado termo
# Autor: Eduardo Knop

n1 = float(input('Escolha o 1° Termo da Progressão Aritmética: '))
p = float(input('Escolha o passo da Progressão Aritmética: '))
nv = 0

while nv < 10:
    if nv < 9:
        print(n1, end=' → ')
    else:
        print(n1)
    n1 += p
    nv += 1
