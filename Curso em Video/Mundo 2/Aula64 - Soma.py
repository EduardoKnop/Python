# Aula Laços de Repetição Pt 2
# Este programa realiza a soma de todos os números digitados
# Autor: Eduardo Knop

n1 = float(input('Digite o 1° Número: '))
n2 = 0.0
i = 0
soma = n1
while n2 != 999:
    soma += n2
    i += 1
    n2 = float(input('Digite outro número ou [ 999 ] para sair: '))
print('A soma foi: {}\n{} números foram digitados.'.format(soma, i))
