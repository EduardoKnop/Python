# Aula Laços de Repetição Pt 2
# Este programa calcula a média, o menor e o maior valor digitado pelo usuário
# Autor: Eduardo Knop

num = float(input('Digite o 1° Valor: '))
soma = menor = maior = num
media = 1.0
user = str(input('Digite [ S ] para continuar ou outro valor para sair: '))[0]

while user in 'Ss':
    media += 1
    num = float(input('Digite o {}° valor: '.format(media)))
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    user = str(input('Quer continuar? [S/N] ')).strip()[0]
media = soma / media
print('\nMaior: {}\nMenor: {}\nMédia: {}'.format(maior, menor, media))
