from asyncio import events
import pygame
import random
import time

class Jogo:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 600))
        self.botao = pygame.image.load('Botao.png')
        texto = pygame.font.SysFont('Stencil', 65)
        self.screen.blit(texto.render('MINESWEEPER', False, (255, 255, 255)), (30, 50))
        texto = pygame.font.SysFont('Stencil', 48)
        self.screen.blit(self.botao, (51, 150))
        self.screen.blit(texto.render('Fácil', False, (0, 0, 0)), (180, 189))
        self.screen.blit(self.botao, (51, 300))
        self.screen.blit(texto.render('Intermediário', False, (0, 0, 0)), (65, 339))
        self.screen.blit(self.botao, (51, 450))
        self.screen.blit(texto.render('Difícil', False, (0, 0, 0)), (170, 489))
        pygame.display.flip()
    

    def iniciar(self) -> str:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 'SAIR'
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse = pygame.mouse.get_pos()
                    if 51 <= pos_mouse[0] <= 449:
                        if 150 < pos_mouse[1] <= 277:
                            return 'FACIL'
                        elif 300 < pos_mouse[1] <= 427:
                            return 'MEDIO'
                        elif 450 < pos_mouse[1] <= 577:
                            return 'DIFICIL'
    

    def criar_tabuleiro(self, dificuldade):
        self.tabuleiro = []
        mina = []

        self.tijolo = pygame.image.load('Tijolo.png')
        self.tijolos = {'mina': pygame.image.load('Mina.png'),
                        'explodida': pygame.image.load('Mina_explodida.png'),
                        'indicador': pygame.image.load('Indicador.png')}
        self.vazio = (pygame.image.load('0.png'), pygame.image.load('1.png'),
                      pygame.image.load('2.png'), pygame.image.load('3.png'),
                      pygame.image.load('4.png'), pygame.image.load('5.png'),
                      pygame.image.load('6.png'))

        if dificuldade == 'FACIL':
            self.screen = pygame.display.set_mode((315, 315))
            limite = (315, 315)
            dificuldade = 1
            self.quant_tijolos = 81
        elif dificuldade == 'MEDIO':
            self.screen = pygame.display.set_mode((560, 560))
            limite = (560, 560)
            dificuldade = 2
            self.quant_tijolos = 256
        elif dificuldade == 'DIFICIL':
            self.screen = pygame.display.set_mode((1050, 560))
            limite = (1050, 560)
            dificuldade = 4
            self.quant_tijolos = 480

        while len(mina) != dificuldade:
            m = random.randint(0, 9)
            if m in mina:
                continue
            mina.append(m)

        quant_minas = 0
        for y in range(0, limite[1], 35):
            self.tabuleiro.append([])
            for x in range(0, limite[0], 35):
                self.tabuleiro[y // 35].append(random.randint(0, 9))
                self.screen.blit(self.tijolo, (x, y))
                for n in mina:
                    if n == self.tabuleiro[y // 35][x // 35]:
                        self.tabuleiro[y // 35][x // 35] = 'MINA'
                        quant_minas += 1
                        continue
                    elif self.tabuleiro[y // 35][x // 35] == 'MINA':
                        continue
                    self.tabuleiro[y // 35][x // 35] = '0'
        self.quant_tijolos -= quant_minas

        for y in range(len(self.tabuleiro)):
            for x in range(len(self.tabuleiro[y])):
                if self.tabuleiro[y][x] == 'MINA':
                    if x > 0:
                        if self.tabuleiro[y][x - 1] != 'MINA':
                            self.tabuleiro[y][x - 1] = str(int(self.tabuleiro[y][x - 1]) + 1)
                    if x < len(self.tabuleiro[y]) - 1:
                        if self.tabuleiro[y][x + 1] != 'MINA':
                            self.tabuleiro[y][x + 1] = str(int(self.tabuleiro[y][x + 1]) + 1)
                    if y > 0:
                        if self.tabuleiro[y - 1][x] != 'MINA':
                            self.tabuleiro[y - 1][x] = str(int(self.tabuleiro[y - 1][x]) + 1)
                    if y < len(self.tabuleiro) - 1:
                        if self.tabuleiro[y + 1][x] != 'MINA':
                            self.tabuleiro[y + 1][x] = str(int(self.tabuleiro[y + 1][x]) + 1)
                    if x > 0 and y > 0:
                        if self.tabuleiro[y - 1][x - 1] != 'MINA':
                            self.tabuleiro[y - 1][x - 1] = str(int(self.tabuleiro[y - 1][x - 1]) + 1)
                    if x > 0 and y < len(self.tabuleiro) - 1:
                        if self.tabuleiro[y + 1][x - 1] != 'MINA':
                            self.tabuleiro[y + 1][x - 1] = str(int(self.tabuleiro[y + 1][x - 1]) + 1)
                    if x < len(self.tabuleiro[y]) - 1 and y > 0:
                        if self.tabuleiro[y - 1][x + 1] != 'MINA':
                            self.tabuleiro[y - 1][x + 1] = str(int(self.tabuleiro[y - 1][x + 1]) + 1)
                    if x < len(self.tabuleiro[y]) - 1 and y < len(self.tabuleiro) - 1:
                        if self.tabuleiro[y + 1][x + 1] != 'MINA':
                            self.tabuleiro[y + 1][x + 1] = str(int(self.tabuleiro[y + 1][x + 1]) + 1)

        pygame.display.flip()

        return self.jogada()


    def jogada(self) -> str:
        while True:
            pygame.display.flip()

            if self.quant_tijolos == 0:
                return 'GANHOU'
            
            mouse, pos_tabuleiro, pos_mouse = self.get_pos()
            y_tabuleiro, x_tabuleiro = pos_tabuleiro
            if mouse == 'ESQUERDO' and 'B' not in self.tabuleiro[y_tabuleiro][x_tabuleiro]:
                if self.tabuleiro[y_tabuleiro][x_tabuleiro] != 'MINA':
                    self.screen.blit(self.vazio[int(self.tabuleiro[y_tabuleiro][x_tabuleiro])], (pos_mouse))
                    self.quant_tijolos -= 1
                else:
                    for y in range(len(self.tabuleiro)):
                        for x in range(len(self.tabuleiro[y])):
                            if self.tabuleiro[y][x] == 'MINA':
                                self.screen.blit(self.tijolos['mina'], (x * 35, y * 35))
                    self.screen.blit(self.tijolos['explodida'], (pos_mouse))
                    pygame.display.flip()
                    time.sleep(3)

                    return 'PERDEU'
            elif mouse == 'DIREITO' and 'X' not in self.tabuleiro[y_tabuleiro][x_tabuleiro]:
                if 'B' in self.tabuleiro[y_tabuleiro][x_tabuleiro]:
                    self.screen.blit(self.tijolo, (pos_mouse))
                    self.tabuleiro[y_tabuleiro][x_tabuleiro] = self.tabuleiro[y_tabuleiro][x_tabuleiro].replace('B', '')
                    continue
                self.screen.blit(self.tijolos['indicador'], (pos_mouse))
                self.tabuleiro[y_tabuleiro][x_tabuleiro] += 'B'
    

    def get_pos(self) -> tuple:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos_tabuleiro = []

                    bot_mouse = pygame.mouse.get_pressed()
                    pos_mouse = pygame.mouse.get_pos()
                    pos_tabuleiro.append(pos_mouse[0] // 35)
                    pos_tabuleiro.append(pos_mouse[1] // 35)
                    pos_mouse = (pos_mouse[0] - pos_mouse[0] % 35,
                                 pos_mouse[1] - pos_mouse[1] % 35)

                    if bot_mouse == (True, False, False):
                        return 'ESQUERDO', pos_tabuleiro, pos_mouse
                    elif bot_mouse == (False, False, True):
                        return 'DIREITO', pos_tabuleiro, pos_mouse
