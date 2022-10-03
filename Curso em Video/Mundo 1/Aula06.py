# Aula Operações Aritméticas
# Este programa mostra o antecessor, o sucessor, o dobro, o triplo e a raiz quadrada de um número
# Criado por Eduardo Knop

print('--- Este programa mostra o Sucessor, o Antecessor, o Dobro, o Triplo e a Raiz Quadrada de um Número ---')
num = int(input('Digite um número: '))
print('O antecessor de {} é {}\nO sucessor de {} é {}\nO dobro de {} é {}'.format(num, num-1, num, num+1, num, num*2))
print('O triplo de {} é {}\nA Raiz Quadrada de {} é {:.5f}'.format(num, num*3, num, pow(num, 1/2)))
