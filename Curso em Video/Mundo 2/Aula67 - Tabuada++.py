# Aula Laços de Repetição Pt 3
# Este programa mostra a tabuada dos números positivos solicitados
# Autor: Eduardo Knop

cont = 0

print('Este programa mostra a tabuada dos números solicitados')

n = int(input('Selecione o número: '))
while n >= 0:
    cont += 1
    print(f'{n} x {cont:<2} = {n*cont:<2}')
    if cont == 10:
        print('=-' * 12)
        n = int(input('Selecione outro número: '))
        cont = 0
print('Programa Encerrado!')
