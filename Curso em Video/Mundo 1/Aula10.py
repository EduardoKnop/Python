# Aula Operadores Aritméticos
# Este programa converte Reais em Doláres Estadunidenses
# Autor Eduardo Knop

print('Este programa mostra quantos dólares você pode comprar \nUtilizar ponto (.) para separar os centavos')
real = float(input('Quantos reais você possui? R$ '))
cotacao = float(input('Qual a cotação do dólar no dia de hoje? R$ '))
print(f'Você consegue comprar US${real/cotacao:.2f}')
