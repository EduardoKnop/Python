# Aula String
# Este programa lê o nome de uma pessoa e mostra seu primeiro e último nome separadamente
# Autor: Eduardo Knop

print('\n\n*-* Este programa lê o nome de uma pessoa e mostra seu primeiro e último nome separadamente *-*\n\n')

nome = input('Digite seu nome: ')
nome = nome.strip().title()
name = nome.split()

print('\nPrimeiro nome: {} \nÚltimo nome: {}'.format(name[0], name[len(name) - 1]))
