# Aula Laços de Repetição - Pt 2
# Este programa lê o sexo de uma pessoa, se ela digitar errado, repete
# Autor: Eduardo Knop

sex = {'M': 'Masculino',
       'F': 'Feminino'
       }
sexo = ''
c = 1

while sexo != 'M' and sexo != 'F':
    if c > 1:
        print('Você está digitando errado, tente novamente!')
    sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
    c += 1
print('Você é do sexo {}.'.format(sex[sexo]))
