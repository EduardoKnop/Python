# Este programa mostra as informações de um texto digitado

var = input('Digite algo: ')

print(type(var))

print('{} é Alfanumérico? {}'.format(var, var.isalnum()))
print('{} é Alfabético? {}'.format(var, var.isalpha()))
print('{} é Numérico? {}'.format(var, var.isnumeric()))
print('{} é UpperCase? {}'.format(var, var.isupper()))
print('{} é LowerCase? {}'.format(var, var.islower()))
print('{} está Capitalizado? {}'.format(var, var.istitle()))
