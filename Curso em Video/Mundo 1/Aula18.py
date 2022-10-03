# Aula Módulos
# Este Programa informa os valores de Seno, Cosseno e Tangente para um dado Ângulo
# Autor: Eduardo Knop

from math import sin, cos, tan, radians

print('\n\nEste Programa informa os valores de Seno, Cosseno e Tangente para um dado Ângulo\n\n')
ang = float(input('Qual o valor do Ângulo? '))
ang1 = radians(ang)
print('{}° possui:\n Seno = {:.2f}\n Cosseno = {:.2f}\n Tangente = {:.2f}'.format(ang, sin(ang1), cos(ang1), tan(ang1)))
