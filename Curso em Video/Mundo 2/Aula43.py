# Aula Condições Aninhadas
# Este programa calcula o IMC e seu status
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;93m',
       'b': '\033[1;34m',
       'o': '\033[1;33m'
       }

print('{}\n\n*-* Este programa calcula o IMC e seu status *-*\n\n{}'.format(cor['b'], cor['l']))

peso = str(input('Qual seu peso? ')).replace('kg', '').replace(',', '.')
peso = float(peso.strip())
alt = str(input('Qual sua altura? ')).replace('m', '').replace(',', '.')
alt = float(alt.strip())
imc = peso / alt ** 2

print('\nIMC: {:.1f}'.format(imc))
if imc < 18.5:
    print('{}ABAIXO DO PESO{}'.format(cor['r'], cor['l']))
elif 18.5 <= imc <= 25:
    print('{}PESO IDEAL{}'.format(cor['g'], cor['l']))
elif 25 < imc <= 30:
    print('{}SOBREPESO{}'.format(cor['y'], cor['l']))
elif 30 < imc <= 40:
    print('{}OBESIDADE{}'.format(cor['o'], cor['l']))
else:
    print('{}OBESIDADE MÓRBIDA{}'.format(cor['r'], cor['l']))
