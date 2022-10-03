# Aula Módulos
# Este programa diz a hipotenusa de um triângulo retângulo
# Autor: Eduardo Knop

print('\n\nEste programa calcula a hipotenusa de um triângulo retângulo com base em seus catetos\n\n')
cat1 = float(input('Qual o valor do Cateto Oposto? '))
cat2 = float(input('Qual o valor do Cateto Adjacente? '))
hip = pow(cat1 ** 2 + cat2 ** 2, 1/2)
print('Um triângulo retângulo de catetos {:.2f} e {:.2f} tem Hipotenusa igual a {:.2f}'.format(cat1, cat2, hip))
