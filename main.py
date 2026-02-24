import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from menu import Menu
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("洞穴探索游戏")
    
    menu = Menu(screen)
    running = True
    while running:
        menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            selection = menu.handle_event(event)
            if selection == 0:
                # 开始游戏
                game = Game(screen)
                game.run()
            elif selection == 1:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()