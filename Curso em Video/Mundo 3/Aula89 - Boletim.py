# Aula Listas
# Este programa preenche um boletim escolar
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

boletim = []
aluno = []

while True:
    aluno.append(input('Nome: '))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    aluno.append((aluno[1] + aluno[2]) / 2)
    boletim.append(aluno[:])
    aluno.clear()
    op = ' '
    while op not in 'NS':
        op = input('Deseja Continuar? ').strip().upper()[0]
    if op == 'N':
        break

print(f'\t {"Nº":^4} {"ALUNO":^20} {"MÉDIA":^5}')
for i, a in enumerate(boletim):
    print(f'\t {i:^4} {a[0]:<20} {a[3]:^5.2f}')

while True:
    op = int(input('Informe o Nº do Aluno p/ ver detalhes [999 para Sair]: '))
    if op == 999:
        break
    elif op > (len(boletim) - 1) or op < 0:
        print(f'{cor["r"]}Aluno Inexistente!{cor["l"]}\n')
    else:
        print(f'''{cor["b"]}Aluno: {boletim[op][0]}
Nota 1: {boletim[op][1]:<8.2f} Nota 2: {boletim[op][2]:<8.2f}{cor["l"]}''')
        if boletim[op][3] > 70:
            print(f'{cor["g"]}Média:  {boletim[op][3]:<8.2f} ', end='')
            print(f'Situação: APROVADO{cor["l"]}')
        else:
            print(f'{cor["r"]}Média:  {boletim[op][3]:<8.2f} ', end='')
            print(f'Situação: REPROVADO{cor["l"]}')
