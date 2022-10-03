def aumentar(preco=0, taxa=0, format=False):
    preco = preco + preco * taxa / 100
    if format:
        return moeda(preco)
    return preco


def diminuir(preco=0, taxa=0, format=False):
    preco = preco - preco * taxa / 100
    if format:
        return moeda(preco)
    return preco


def dobrar(preco=0, format=False):
    if format:
        return moeda(preco * 2)
    return preco * 2


def metade(preco=0, format=False):
    if format:
        return moeda(preco / 2)
    return preco / 2


def moeda(valor=0):
    return f'R$ {valor:.2f}'


def resumo(preco=0, aumento=0, reducao=0):
    print('-' * 35)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 35)
    print(f'''Preço Analisado: \t{moeda(preco):}
Dobro do Preço: \t{dobrar(preco, True)}
Metade do Preço: \t{metade(preco, True)}
{aumento:<3}% de Aumento: \t{aumentar(preco, aumento, True)}
{reducao:<3}% de Redução: \t{diminuir(preco, reducao, True)}''')
    print('-' * 35)
