# Aula Laços de Repetição Pt 3
# Este programa lê e informa dados sobre uma compra realizada
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[31m',
       'g': '\033[32m',
       'y': '\033[33m'
       }

print('\n\n')
print('*-* Este programa lê e informa dados sobre uma compra realizada *-*\n')

total = quant = caro = 0
stop = 'S'

while True:
    produto = str(input('\nNome do Produto: ')).strip().capitalize()
    preco = float(input('Preço do Produto: R$'))
    if quant == 0 or preco < cheaper:
        barato = produto
        cheaper = preco
    elif preco == cheaper:
        barato = barato + '{} e {}'.format(cor['y'], cor['l']) + produto
    total = total + preco
    quant += 1

    if preco > 1000:
        caro += 1

    stop = str(input('Você quer adicionar um novo produto? [S/N] '))
    if stop in 'Nn':
        break
    elif stop not in 'Ss':
        stop = str(input('Você quer adicionar um novo produto? [S/N] '))

print(f'''{cor['y']}\n\n-=-=- Resumo da Compra -=-=-\n{cor['l']}
{quant} Produtos comprados no Valor Total de {cor['r']}R${total:.2f}{cor['l']}
{caro} Produtos comprados com Valor superior a {cor['r']}R$1000
{cor['g']}Produto mais Barato:{ cor['l']} {barato}''')
