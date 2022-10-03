import moeda
import dados

p = dados.leiaDinheiro('Preço: ')
print(f'A metade de {moeda.moeda(p)} = {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} = {moeda.dobrar(p, True)}')
print(f'Aumentando em 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo em 13%, temos {moeda.diminuir(p, 13, True)}')

moeda.resumo(p, 35, 22)
