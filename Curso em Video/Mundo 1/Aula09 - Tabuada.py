# Aula Operadores Aritméticos
# Este programa mostrará a tabuada do número escolhido
# Autor: Eduardo Knop

i = 1

print('Este programa mostrará a tabuada do número escolhido')
tab = int(input('Você quer a tabuada de qual número? '))

while i <= 10:
    print('{:>2} x {:>2} = {:>3}'.format(tab, i, tab*i))
    i = i + 1
