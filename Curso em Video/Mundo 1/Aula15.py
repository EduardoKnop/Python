# Aula Operadores Aritméticos
# Este programa calcula o preço do aluguel de um carro
# Autor: Eduardo Knop

print('\n\n--- Este programa calculará o preço do aluguel de um carro baseado nos dias e km rodados ---\n\n')
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
preco = 60 * dias + km * 0.15
print('Você deve pagar R${:.2f}'.format(preco))
