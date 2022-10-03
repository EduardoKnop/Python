# Aula Operadores Aritméticos
# Este programa calcula quantos litros de tinta são necessários para pintar uma parede
# Autor: Eduardo Knop

print('-----Este programa calcula quantos litros de tinta são necessários para pintar uma parede-----')

larg = float(input('Qual a largura da parede (em metros)? '))
alt = float(input('Qual a altura dessa parede (em metros)? '))
rend = float(input('Quantos m² pinta cada litro de tinta? '))
area = larg * alt

print('Sua parede de {:.5f} m² precisa de {:.5f} L de tinta'.format(area, area*(rend**-1)))
