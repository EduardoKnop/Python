# Aula Laços de Repetição Pt 3
# Este programa soma os valores até digitar o Flag
# Autor: Eduardo Knop

cont = n = s = 0

print('Este programa soma os valores digitados')

while True:
    n = float(input('Digite um número ou [ 999 ] para parar: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Os {cont} números digitados têm soma igual a {s}')
