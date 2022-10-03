# Aula Funções
# Este programa
# Autor: Eduardo Knop


def fatorial(v, s=False):
    """=> Calcula o fatorial de um número.
    :param v: O número a ser calculado
    :param s: (Opcional) Mostra a conta se True, padrão é False
    :return: O valor do Fatorial do número passado
    """
    r = 1
    print(f'{cor["y"]}{v}!{cor["l"]} = ', end='')
    for k in range(v, 0, -1):
        r *= k
        if s:
            if k > 1:
                print(f'{cor["b"]}{k} X ', end='')
            else:
                print(f'{cor["b"]}{k}{cor["l"]} = ', end='')
    print(f'{cor["g"]}{r}{cor["l"]}')
    return r


cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

while True:
    valor = int(input('Valor: '))
    show = op = ' '
    while show not in 'NS':
        show = input('Deseja mostrar o Cálculo? ').upper().strip()[0]
    if show == 'S':
        fatorial(valor, True)
    else:
        fatorial(valor)
    while op not in 'NS':
        op = input('Deseja Continuar? ').upper().strip()[0]
    if op == 'N':
        break
