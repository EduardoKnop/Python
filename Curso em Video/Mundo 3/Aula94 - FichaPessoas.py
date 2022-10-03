# Aula Listas
# Este programa preenche uma ficha de várias pessoas
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }
ficha = {}

pessoas = []

med = 0

while True:
    ficha['Nome'] = input('Nome: ')
    ficha['Sexo'] = op = ' '
    while ficha['Sexo'] not in 'MF':
        ficha['Sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
    ficha['Idade'] = int(input('Idade: '))
    pessoas.append(ficha.copy())
    ficha.clear()
    while op not in 'SN':
        op = input('Deseja Continuar? ').strip().upper()[0]
    if op == 'N':
        break

for p in pessoas:
    med += p['Idade']
med = med / len(pessoas)

print(f'''\nForam cadastradas {len(pessoas)} Pessoas
A Média de Idade do Grupo é de {med} anos
As Mulheres cadastradas foram: ''', end='')
for p in pessoas:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end='')
print(f'\nAs pessoas acima da média de idade de {med} anos são:')
for p in pessoas:
    if p['Idade'] > med:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
