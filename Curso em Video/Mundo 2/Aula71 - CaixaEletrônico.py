# Aula Laços de Repetição Pt 3
# Este programa simula um Saque no Caixa Eletrônico
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

print('\n\n*-* Este programa simula um Saque no Caixa Eletrônico *-*\n\n')

cedulas50 = cedulas20 = cedulas10 = cedulas1 = 0
print('{}Olá, Seja bem Vindo ao Caixa do Banco{}'.format(cor['b'], cor['l']))
op = str(input('''Selecione a Operação Desejada:
[ C ] Saque do Cartão de Crédito
[ D ] Saque da Conta\n'''))
valor = int(input('Qual o Valor a ser Sacado? R$'))
cedulas50 = valor // 50
valor = valor - cedulas50 * 50
cedulas20 = valor // 20
valor = valor - cedulas20 * 20
cedulas10 = valor // 10
valor = valor - cedulas10 * 10
cedulas1 = valor

print(f'''{cor['y']}*** Operação Finalizada ***
{cor['b']}{cedulas50}{cor['l']} Cédulas de 50 Sacadas
{cor['b']}{cedulas20}{cor['l']} Cédulas de 20 Sacadas
{cor['b']}{cedulas10}{cor['l']} Cédulas de 10 Sacadas
{cor['b']}{cedulas1}{cor['l']} Cédulas de 1 Sacadas''')
