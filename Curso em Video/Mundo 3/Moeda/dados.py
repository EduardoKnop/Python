def leiaDinheiro(msg=''):
    while True:
        valor = input(msg).strip().replace(',', '.')
        if valor.count('R$') == 1:
            valor = valor.lstrip('R$').strip()
        num = valor.split('.')
        if len(num) == 1 and num[0].isnumeric():
            return float(valor)
        elif len(num) == 2 and num[0].isnumeric() and num[1].isnumeric():
            return float(valor)
        print('\033[1;31mValor Monetário Inválido\033[m')
