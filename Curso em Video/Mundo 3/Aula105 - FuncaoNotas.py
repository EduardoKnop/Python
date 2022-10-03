# Aula Funções
# Este programa
# Autor: Eduardo Knop


def notas(*n, s=False):
    """=> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos
    :param s: (Parâmetro Opcional) Indica se deve-se adicionar a situação
    :return: Dicionário com vários informações sobre a situação da turma
    """
    b = {}
    b['Quantidade'] = len(n)
    b['Maior'] = max(n)
    b['Menor'] = min(n)
    b['Media'] = (sum(n) / len(n))
    if s and b['Media'] < 50:
        b['Situacao'] = 'RUIM'
    elif s and b['Media'] < 70:
        b['Situacao'] = 'REGULAR'
    elif s:
        b['Situacao'] = 'BOA'
    return b


cor = {'l': '\033[m',
       'r': '\033[1;31m',
       'g': '\033[1;32m',
       'y': '\033[1;33m',
       'b': '\033[1;34m'
       }

boletim = notas(55, 25, 10, 65)
print(boletim)
