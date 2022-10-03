# Aula Tuplas
# Este programa mostra infos da tabela do Brasileirao 2020
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

tabela = ('Flamengo', 'Internacional', 'Atlético', 'São Paulo', 'Fluminense',
          'Grêmio', 'Palmeiras', 'Santos', 'Athletico', 'Bragantino',
          'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport',
          'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')

print('\n\n{}*-* Este programa mostra infos do Brasileirão 2020 *-*{}\n'.format(cor['y'], cor['l']))

while True:
    op = input(f'''\nEscolha a informação a ser exibida:
    {cor['g']}[ G4 ] Exibe os 4 primeiros colocados
    {cor['b']}[ G6 ] Exibe os 6 primeiros colocados
    {cor['r']}[ Z4 ] Exibe os 4 rebaixados
    {cor['y']}[ A ] Exibe os times em ordem alfabética
    ou Escreva o Nome do Time para exibir sua posição{cor['l']}
    ''')
    op = op.title().strip()

    if op == 'G4':
        for i in range(0, 4):
            print(cor['g'] + tabela[i])
        print(cor['l'])
    elif op == 'G6':
        for i in range(0, 6):
            print(cor['b'] + tabela[i])
        print(cor['l'])
    elif op == 'Z4':
        for i in range(16, 20):
            print(cor['r'] + tabela[i])
        print(cor['l'])
    elif op == 'A':
        print(sorted(tabela))
    elif op in tabela:
        print(f'''{cor['b']}{tabela.index(op) + 1}º Colocado{cor['l']}''')
    else:
        break
