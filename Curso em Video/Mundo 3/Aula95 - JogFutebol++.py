# Aula Listas
# Este programa preenche dados de vários jogadores de futebol
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }
jog = {}

pessoas = []

while True:
    jog['Nome'] = input('Nome do Jogador: ')
    part = int(input(f'Quantas partidas {jog["Nome"]} jogou? '))
    jog['Gols'] = list()
    for p in range(0, part):
        jog['Gols'].append(int(input(f'Quantos gols na partida {p + 1}? ')))
    jog['Total'] = sum(jog['Gols'])
    pessoas.append(jog.copy())
    jog.clear()
    op = ' '
    if op not in 'NS':
        op = input('Deseja Continuar? ').strip().upper()[0]
    print('-' * 30)
    if op == 'N':
        break
print(f'{cor["y"]}\t{"Nº"} {"Nome":^10} {"Gols":^15} {"Total"}')
for i, j in enumerate(pessoas):
    print(f'{cor["b"]}\t{i:<2} {j["Nome"]:<10} {j["Gols"]} {j["Total"]:^5}')
print(f'{cor["l"]}', end='')

while True:
    op = int(input('Digite o Nº do Jogador do qual deseja ver mais dados: '))
    if 0 <= op < len(pessoas):
        print(f'{cor["y"]}LEVANTAMENTO DO JOGADOR {pessoas[op]["Nome"]}')
        for i, g in enumerate(pessoas[op]['Gols']):
            print(f'\t=> Na Partida {i + 1}, fez {g} Gols.')
        print(f'{cor["g"]}Total: {pessoas[op]["Total"]} Gols em ', end='')
        print(f'{len(pessoas[op]["Gols"])} Jogos{cor["l"]}')
    elif op == 999:
        break
    else:
        print(f'{cor["r"]}Número Inválido! Tente Novamente{cor["l"]}')
    print('=-' * 14)
