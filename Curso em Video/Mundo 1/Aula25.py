# Aula String
# Este programa informa se uma dada pessoa tem 'Silva' no nome
# Autor: Eduardo Knop

print('\n\n*-* Este programa informa se uma dada pessoa possui Silva no nome *-*\n\n')

nome = input('Digite um nome: ')
nome = nome.strip().title()
name = nome.lower().split()

print('{} possui Silva no nome? {}'.format(nome, 'silva' in name))
