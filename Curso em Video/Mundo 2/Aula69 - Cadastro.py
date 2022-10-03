# Aula Laços de Repetição Pt 3
# Este programa cria um cadastro de pessoas e retorna alguns dados
# Autor: Eduardo Knop

from time import sleep

idade18 = homem = menina = cont = 0

while True:
    idade = int(input(f'Idade da {cont + 1}ª Pessoa: '))
    sexo = str(input(f'Sexo da {cont + 1}ª Pessoa [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Tente novamente [M/F]: ')).upper().strip()[0]
    if idade > 18:
        idade18 += 1
    if sexo in 'M':
        homem += 1
    if sexo in 'F' and idade < 20:
        menina += 1
    stop = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while stop not in 'SN':
        stop = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if stop in 'N':
        break
    cont += 1

print('Analisando...')
sleep(1)
print(f'''Das {cont + 1} pessoas analisadas:
    {idade18} são maiores de idade;
    {homem} são homens; e
    {menina} são mulheres menores de 20.''')
