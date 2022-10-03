# Aula Listas
# Este programa
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

posAbre = []
posFecha = []
inv = False

expressao = [input('Digite a Expressão: ')]
print(expressao)
expressao.append(expressao[0].count('('))
expressao.append(expressao[0].count(')'))
if expressao[1] != expressao[2]:
    inv = True
else:
    expressao.append(posAbre)
    expressao.append(posFecha)
    for count, verify in enumerate(expressao[0]):
        if verify == '(':
            posAbre.append(count)
        elif verify == ')':
            posFecha.append(count)
    for count, verify in enumerate(posFecha):
        if verify < posAbre[count]:
            inv = True

if inv is False:
    print(f'{cor["g"]}Expressão Válida!!!{cor["l"]}')
else:
    print(f'{cor["r"]}Expressão Inválida!{cor["l"]}')
