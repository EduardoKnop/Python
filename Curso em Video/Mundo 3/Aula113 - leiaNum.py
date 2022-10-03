c = {'l': '\033[m',
     'r': '\033[1;31m',
     'g': '\033[1;32m',
     'y': '\033[1;33m',
     'b': '\033[1;34m'
     }


def leiaInt(msg=''):
    while True:
        try:
            num = int(input(msg))
        except Exception:
            print(f'{c["r"]}ERROR 404. Número not found{c["l"]}')
        else:
            return num


def leiaFloat(msg=''):
    while True:
        try:
            num = float(input(msg).replace(',', '.'))
        except Exception:
            print(f'{c["r"]}ERROR 404. Número not found{c["l"]}')
        else:
            return num
