import pygame
from ui.menu import Menu
from ui.game import Game
from ui.end import End

def main():
    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Tic Tac Toe')

    menu = Menu(screen)
    game = Game(screen)
    end = End(screen)

    running = True
    state = 'MENU'
    winner = None

    while running:
        if state == 'MENU':
            state = menu.run()
        elif state == 'GAME':
            state, winner = game.run()
        elif state == 'END':
            state = end.run(winner)
        elif state == 'QUIT':
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
