import pygame
from interfaces.game_interface import GameInterface
from interfaces.event_custom import EVENT_GAME_END
from logic.game_logic import GameLogic

class Game(GameInterface):
    def __init__(self, screen):
        self.screen = screen
        self.logic = GameLogic()

    def run(self):
        running = True
        winner = None
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'QUIT', None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row, col = y // 200, x // 200
                    if self.logic.make_move(row, col):
                        winner = self.logic.check_winner()
                        if winner or self.logic.is_draw():
                            pygame.event.post(pygame.event.Event(EVENT_GAME_END))
                            return 'END', winner

            self.screen.fill((255, 255, 255))
            self.draw_board()
            pygame.display.flip()

    def draw_board(self):
        for row in range(3):
            for col in range(3):
                x = col * 200
                y = row * 200
                pygame.draw.rect(self.screen, (0, 0, 0), (x, y, 200, 200), 3)
                if self.logic.board[row][col] == 'X':
                    pygame.draw.line(self.screen, (255, 0, 0), (x, y), (x + 200, y + 200), 3)  # Red X
                    pygame.draw.line(self.screen, (255, 0, 0), (x + 200, y), (x, y + 200), 3)
                elif self.logic.board[row][col] == 'O':
                    pygame.draw.circle(self.screen, (0, 0, 255), (x + 100, y + 100), 90, 3)  # Blue O
