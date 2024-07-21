import pygame
from interfaces.end_interface import EndInterface

class End(EndInterface):
    def __init__(self, screen):
        self.screen = screen

    def run(self, winner):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'QUIT'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 'MENU'

            self.screen.fill((255, 255, 255))
            self.draw_end_screen(winner)
            pygame.display.flip()

    def draw_end_screen(self, winner):
        font = pygame.font.Font(None, 74)
        if winner:
            text = font.render(f'{winner} Wins!', True, (0, 0, 0))
        else:
            text = font.render('Draw!', True, (0, 0, 0))
        self.screen.blit(text, (150, 250))
        text = font.render('Click to Restart', True, (0, 0, 0))
        self.screen.blit(text, (150, 350))
