# Aula Listas
# Este programa cria uma lista com nome e pesos das pessoas
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

pop = []
pessoa = []

while True:
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso (Kg): ')))
    if len(pop) == 0:
        maxi = mini = pessoa[1]
    elif pessoa[1] > maxi:
        maxi = pessoa[1]
    elif pessoa[1] < mini:
        mini = pessoa[1]
    pop.append(pessoa[:])
    pessoa.clear()
    op = ' '
    if op not in 'SN':
        op = input('Deseja continuar? ').upper().strip()[0]
    if op == 'N':
        break

print(pop)
print(f'\n\nQuantidade de pessoas cadastradas: {len(pop)}')
print(f'Pessoas mais Pesadas ({maxi} kg): {cor["r"]}', end='')
for p in pop:
    if p[1] == maxi:
        print(f'{p[0]} ', end='')
print(f'\n{cor["l"]}Pessoas mais Leves ({mini} kg) e são: {cor["g"]}', end='')
for p in pop:
    if p[1] == mini:
        print(f'{p[0]} ', end='')
