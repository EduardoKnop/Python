# Aula Listas
# Este programa preenche dados de um jogador de futebol
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }
jog = {}

jog['Nome'] = input('Nome do Jogador: ')
part = int(input(f'Quantas partidas {jog["Nome"]} jogou? '))
jog['Gols'] = list()
for p in range(0, part):
    jog['Gols'].append(int(input(f'Quantos gols na partida {p + 1}? ')))
jog['Total'] = sum(jog['Gols'])
print(f'''
{jog["Nome"]} fez um total de {jog["Total"]} Gols em {part} Partidas:''')
for i, g in enumerate(jog['Gols']):
    print(f'    => Na Partida {i + 1}, fez {g} Gols.')
