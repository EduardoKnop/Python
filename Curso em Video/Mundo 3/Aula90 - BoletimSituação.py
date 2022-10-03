# Aula Listas
# Este programa preenche um boletim individual
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

ficha = {}

ficha['Nome'] = input('Nome: ')
ficha['Media'] = float(input(f'Média de {ficha["Nome"]}: '))
if ficha['Media'] < 50:
    ficha['Situacao'] = f'{cor["r"]}REPROVADO{cor["l"]}'
elif ficha['Media'] < 70:
    ficha['Situacao'] = f'{cor["y"]}RECUPERAÇÃO{cor["l"]}'
else:
    ficha['Situacao'] = f'{cor["g"]}APROVADO{cor["l"]}'
print(f'''\nA Média de {ficha["Nome"]} é {ficha["Media"]}
Sua situação é {ficha["Situacao"]}''')
