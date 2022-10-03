import minesweeper

op = 'S'
while op != 'N':
    a = minesweeper.Jogo()
    b = a.criar_tabuleiro(a.iniciar())
    if b == 'GANHOU':
        print('Parabéns você GANHOU!')
    elif b == 'PERDEU':
        print('Infelizmente você perdeu :(')
    op = input('Gostaria de jogar novamente? ')[0].upper()
