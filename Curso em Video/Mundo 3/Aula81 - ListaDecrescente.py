# Aula Listas
# Este programa obtem uma lista e a organiza de forma decrescente
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

valores = []
c = 1

while True:
    valores.append(int(input(f'Informe o {c}º Valor: ')))
    op = ' '
    while op not in 'NS':
        op = input('Deseja Continuar? ').upper().strip()[0]
    if op == 'N':
        break
    else:
        c += 1

valores.sort(reverse=True)
print(f'Foram digitados {c} números que formaram a Lista: {valores}')
if 5 in valores:
    print(f'{cor["g"]}O número 5 faz parte desta lista!{cor["l"]}')
else:
    print(f'{cor["r"]}O número 5 não faz parte desta lista!{cor["l"]}')
