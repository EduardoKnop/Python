# Aula Laços de Repetição
# Este programa é um jogo de Par ou Ímpar
# Autor: Eduardo Knop

from random import randint

cont = 0

print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 15)

while True:
    comp = randint(0, 10)
    user = int(input('Escolha um valor: '))
    jogo = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    s = user + comp
    print(f'Você escolheu {user} e o computador {comp} e a soma é {s}')
    if s % 2 == 0:
        result = 'P'
    else:
        result = 'I'

    if jogo == result:
        print('VOCÊ GANHOU!!! Parabéns!')
        print('=-' * 15)
        cont += 1
    else:
        print('VOCÊ PERDEU')
        break
print(f'\nVocê conseguiu ganhar {cont} vezes consecutivas')
