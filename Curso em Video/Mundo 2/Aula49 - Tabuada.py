# Aula Laços de Repetição
# Este programa mostrará a tabuada do número escolhido
# Autor: Eduardo Knop

print('Este programa mostrará a tabuada do número escolhido')
tab = int(input('Você quer a tabuada de qual número? '))

for i in range(1, 11):
    print('{:>2} x {:>2} = {:>3}'.format(tab, i, tab*i))
