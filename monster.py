import pygame
import random

class Monster:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x * 32, self.y * 32)
    
    def move_ai(self, player, dungeon_map):
        # 简单AI：朝玩家移动，随机
        dx, dy = 0, 0
        if random.random() < 0.5:
            if player.x > self.x:
                dx = 1
            elif player.x < self.x:
                dx = -1
            else:
                dx = 0
        else:
            if player.y > self.y:
                dy = 1
            elif player.y < self.y:
                dy = -1
            else:
                dy = 0
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < len(dungeon_map[0]) and 0 <= ny < len(dungeon_map):
            if dungeon_map[ny][nx] == 0:
                self.x, self.y = nx, ny
                self.rect.topleft = (self.x * 32, self.y * 32)
    
    def draw(self, screen):
        screen.blit(self.img, self.rect)