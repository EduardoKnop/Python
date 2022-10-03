# Aula Operadores Numéricos
# Este programa transforma um valor em °C para °F e K
# Autor: Eduardo Knop

print('----- Este programa transformará a temperatura em °C para °F e K -----')
celsius = float(input('Informe uma temperatura em °C: '))
f = celsius / 5 * 9 + 32
k = celsius + 273.15
print('{} °C correspondem a: \n{:>30.2f} °F \n{:>30.2f} K'.format(celsius, f, k))
