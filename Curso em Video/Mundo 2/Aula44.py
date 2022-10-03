# Aula Condições Aninhadas
# Este programa calcula o valor de um produto
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m'
       }

print('\n\n{}*-* Este programa calcula descontos e taxas no valor de um produto *-*{}\n\n'.format(cor['y'], cor['l']))

price = float(input('Qual o valor do produto? R$ '))
print('Qual o meio de pagamento? Digite:\n• 1 p/ Dinheiro\n• 2 p/ Cheque')
print('• 3 p/ Cartão')
pag = int(input())

if pag == 1 or pag == 2:
    price = 0.9 * price
    print('{}10% OFF{}, o preço é R$ {:.2f}'.format(cor['g'], cor['l'], price))
elif pag == 3:
    parc = int(input('Em quantas vezes? '))
    if parc == 1:
        price = 0.95 * price
        print('{}5% OFF{}, o preço é R$ {:.2f}'.format(cor['g'], cor['l'], price))
    elif parc == 2:
        print('Não há desconto. O preço é R$ {:.2f}'.format(price))
        print('Sua compra será de R$ {:.2f} por mês'.format(price / parc))
    elif 2 < parc < 13:
        price = 1.2 * price
        print('{}JUROS de 20%{}, o preço é R$ {:.2f}'.format(cor['r'], cor['l'], price))
        print('Sua compra será de R$ {:.2f} por mês'.format(price / parc))
else:
    print('Número Inválido!')
