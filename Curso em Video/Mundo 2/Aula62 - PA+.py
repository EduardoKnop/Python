# Aula Laços de Repetição
# Este programa mostra 10+ termos de uma P.A.
# Autor: Eduardo Knop

n1 = float(input('Digite o 1° Termo: '))
p = float(input('Digite o Passo da Progressão Aritmética: '))
nv = 10

while nv > 0:
    if nv == 1:
        print(n1)
        nv = int(input('Digite o número de termos que quer a mais: ')) + 1
    else:
        print(n1, end=' → ')
    n1 += p
    nv -= 1
print('FIM')
