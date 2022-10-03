# Aula Funções
# Este programa
# Autor: Eduardo Knop

def voto(a):
    from datetime import date

    global i
    i = date.today().year - a
    if i < 0:
        return f'{cor["r"]}INVÁLIDO{cor["l"]}'
    elif i < 16:
        return f'{cor["r"]}NEGADO{cor["l"]}'
    elif i < 18 or i >= 65:
        return f'{cor["b"]}OPCIONAL{cor["l"]}'
    else:
        return f'{cor["g"]}OBRIGATÓRIO{cor["l"]}'


cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

i = 0

while True:
    vot = voto(int(input('Data de Nascimento: ')))
    print(f'Com {i} anos, seu voto é {vot}!!!')
    op = ' '
    while op not in 'NS':
        op = input('Deseja Continuar? ').upper().strip()[0]
    if op in 'N':
        break
