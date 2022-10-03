# Aula Strings
# Este programa te dá infos sobre seu nome
# Autor: Eduardo Knop

print('''\n\nEste programa:
- Transforma seu nome em maiúscula
- Transforma em minúscula
- Conta o número de caracteres
- Conta os caracteres do primeiro nome\n\n''')

nome = input('Qual seu nome completo? ')
nome = nome.strip().title()
print(nome.upper())
print(nome.lower())

num1 = int(len(nome)) - int(nome.count(' '))
print('Seu nome completo tem {} letras'.format(num1))

nome = nome.split()
num2 = int(len(nome[0]))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome[0], num2))
