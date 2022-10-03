# Aula Funções
# Este programa calcula a área de um terreno retangular
# Autor: Eduardo Knop

def area(c, lg):
    a = c * lg
    print(f'{c} m X {lg} m = {a} m²')
    return a


cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

print(f'{"CONTROLE DE TERRENOS":^24}')
print('-=' * 12)
area(float(input('Comprimento (m): ')), float(input('Largura (m): ')))
