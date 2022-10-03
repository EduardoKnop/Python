# Aula Laços de Repetição
# Este programa faz um monte de coisa, preencha o que for pedido
# Autor: Eduardo Knop

media = 0.0
velho = -1
menor = 0

for i in range(0, 4):
    print('\nPreencha as informações da {}ª Pessoa'.format(i + 1))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().title()
    media += idade
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        menor += 1

media /= 4
print('\nA média de idade dessas 4 pessoas é {:.2f} anos'.format(media))
if velho == -1:
    print('Não houveram pessoas do sexo Masculino')
else:
    print('O homem mais velho do grupo se chama {} e tem {} anos'.format(nomeVelho, velho))
print('{} mulher(es) tem menos de 20 anos nesse grupo'.format(menor))
