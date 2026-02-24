import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 40)
        self.selected = 0
        self.options = ["开始游戏", "退出"]
    
    def draw(self):
        self.screen.fill((30, 30, 30))
        for idx, option in enumerate(self.options):
            color = (200, 200, 0) if idx == self.selected else (200, 200, 200)
            text_render = self.font.render(option, True, color)
            self.screen.blit(text_render, (320, 200 + idx * 70))
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.selected
        return None