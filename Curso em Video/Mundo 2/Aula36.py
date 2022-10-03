# Aula Condições Aninhadas
# Este programa informa os valores da prestação ao comprar uma casa
# Autor: Eduardo Knop

cor = {'limpa': '\033[m',
       'red': '\033[31m',
       'green': '\033[32m'
       }

print('\n\n{}*-* Este programa informa os valores da prestação ao comprar uma casa *-*{}\n\n'.format('\033[1;33m', cor['limpa']))

casa = float(input('Qual o valor da casa?{} R$ '.format(cor['red'])))
salario = float(input('{}Qual seu salário? {}R$ '.format(cor['limpa'], cor['green'])))
anos = float(input('{}Em quantos anos você quer pagar? '.format(cor['limpa'])))
mensal = casa / (anos * 12)

if mensal > 0.3 * salario:
    print('\n{}Infelizemente não pudemos aprovar seu pedido{}.'.format(cor['red'], cor['limpa']))
    print('Você pode tentar novamente com uma duração maior ou um valor inferior!')
else:
    print('\nPara comprar essa casa, você terá de pagar {}R$ {:.2f}{} por mês'.format(cor['red'], mensal, cor['limpa']))
