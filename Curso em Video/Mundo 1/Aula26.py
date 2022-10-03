# Aula String
# Este programa conta o número de A`s numa frase, a posição que aparece pela 1ª e última vez
# Autor: Eduardo Knop

print('\n\n*-* Este programa conta o número de A`s numa frase, a posição que aparece pela 1ª e última vez *-*\n\n')

frase = input('Digite uma frase: ')
frase = frase.lower().strip()
print('A frase possui {} letras "A", o primeiro aparece na posição {} e o último na posição {}'.format(frase.count('a'), frase.find('a') + 1, frase.rfind('a') + 1))
