# Aula Operadores Aritméticos
# Este programa aumenta segundo o valor da inflação o salário de um funcionário
# Autor: Eduardo Knop

print('Digite o salário de um funcionário e a inflação deste ano, o programa lhe dirá qual deve ser o novo salário')
inflacao = float(input('Qual a inflação deste ano? '))
print('A inflação é de {}%, correto?'.format(inflacao))
inflacao = inflacao * 0.01
salario = float(input('Qual o salário atual do empregado? R$'))
print('Corrigido pela inflação, o novo salário será de R${:.2f}'.format(salario*(inflacao+1)))
