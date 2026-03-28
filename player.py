import pygame

class Player:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x * 32, self.y * 32)
    
    def move(self, dx, dy, dungeon_map):
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < len(dungeon_map[0]) and 0 <= ny < len(dungeon_map):
            if dungeon_map[ny][nx] == 0:  # 0 是地板，1 是墙
                self.x, self.y = nx, ny
                self.rect.topleft = (self.x * 32, self.y * 32)
    
    def draw(self, screen):
        screen.blit(self.img, self.rect)