import pygame
from interfaces.menu_interface import MenuInterface
from interfaces.event_custom import EVENT_GAME_START


class Menu(MenuInterface):
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'QUIT'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 150 <= x <= 450 and 350 <= y <= 450:
                        pygame.event.post(pygame.event.Event(EVENT_GAME_START))
                        return 'GAME'

            self.screen.fill((173, 216, 230))  # Light Blue Background
            self.draw_menu()
            pygame.display.flip()

    def draw_menu(self):
        font = pygame.font.Font(None, 74)
        text = font.render('Tic Tac Toe', True, (0, 0, 128))  # Navy color
        self.screen.blit(text, (150, 200))

        pygame.draw.rect(self.screen, (0, 0, 128), (150, 350, 300, 100))  # Navy color for button
        font = pygame.font.Font(None, 50)
        text = font.render('Click to Play', True, (255, 255, 255))  # White color text
        self.screen.blit(text, (175, 375))
