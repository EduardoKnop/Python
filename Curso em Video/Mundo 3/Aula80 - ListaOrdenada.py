# Aula Listas
# Este programa ordena a lista durante a digitação
# Autor: Eduardo Knop

cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

valores = []

for c in range(0, 5):
    valores.append(int(input(f'Insira o {c + 1}º Valor: ')))
    if c > 3 and valores[c] < valores[c - 4]:
        valores[c], valores[c - 4] = valores[c - 4], valores[c]
        valores[c], valores[c - 3] = valores[c - 3], valores[c]
        valores[c], valores[c - 2] = valores[c - 2], valores[c]
        valores[c], valores[c - 1] = valores[c - 1], valores[c]
    elif c > 2 and valores[c] < valores[c - 3]:
        valores[c], valores[c - 3] = valores[c - 3], valores[c]
        valores[c], valores[c - 2] = valores[c - 2], valores[c]
        valores[c], valores[c - 1] = valores[c - 1], valores[c]
    elif c > 1 and valores[c] < valores[c - 2]:
        valores[c], valores[c - 2] = valores[c - 2], valores[c]
        valores[c], valores[c - 1] = valores[c - 1], valores[c]
    elif c > 0 and valores[c] < valores[c - 1]:
        valores[c], valores[c - 1] = valores[c - 1], valores[c]
    elif c == 0:
        print(f'Lista iniciada com valor {valores[c]}')
print(valores)
