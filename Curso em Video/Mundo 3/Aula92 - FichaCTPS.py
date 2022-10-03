# Aula Listas
# Este programa preenche uma ficha com dados pessoais
# Autor: Eduardo Knop

from datetime import date

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }
ficha = {}

ficha['Nome'] = input('Nome: ')
nasc = int(input('Ano de Nascimento: '))
ficha['Idade'] = (date.today().year - nasc)
ficha['CTPS'] = int(input('CTPS (Apenas Números) [0 se não tiver]: '))
if ficha['CTPS'] != 0:
    ficha['Contratacao'] = int(input('Ano de Contratação: '))
    ficha['Salario'] = float(input('Salário: R$ '))
    ficha['Aposentar'] = ficha['Contratacao'] + 35 - nasc
    print()
    print(f'''{ficha["Nome"]} tem {ficha["Idade"]} anos, CTPS: {ficha["CTPS"]}
Sua 1ª Contratação foi em {ficha["Contratacao"]}
Atualmente recebe R${ficha["Salario"]:.2f}
E irá se Aposentar com {ficha["Aposentar"]} anos''')
else:
    print(f'\n{ficha["Nome"]}, tem {ficha["Idade"]} anos, não possui CTPS')
