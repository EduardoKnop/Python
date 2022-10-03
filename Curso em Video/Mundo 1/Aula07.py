# Aula Operações Aritméticas
# Este programa lê duas notas de um aluno e calcula a média
# Autor: Eduardo Knop

print('Este programa lê duas notas de um aluno e calcula a média')

nota1 = float(input('Digite a 1ª Nota: '))
nota2 = float(input('Digite a 2ª Nota: '))

print('A média entre {} e {} é {:.2f}'.format(nota1, nota2, (nota1 + nota2)/2))
