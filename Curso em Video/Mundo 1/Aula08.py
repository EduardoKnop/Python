# Aula Operadores Aritméticos
# Este programa converte uma medida em metros para centímetros e milímetros
# Autor: Eduardo Knop

print('------ Este programa converte metros em suas subunidades ------')

metro = float(input('Digite um valor em metros: '))
print('{} m corresponde(m) a:\n{:>30} km\n{:>30} hm\n{:>30} dam'.format(metro, metro/1000, metro/100, metro/10))
print('{:>30} dm\n{:>30} cm\n{:>30} mm'.format(metro*10, metro*100, metro*1000))
