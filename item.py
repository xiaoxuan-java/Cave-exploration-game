import pygame

class Item:
    def __init__(self, x, y, img, picked=False):
        self.x = x
        self.y = y
        self.img = img
        self.picked = picked
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x * 32, self.y * 32)
    
    def draw(self, screen):
        if not self.picked:
            screen.blit(self.img, self.rect)
    
    def try_pick(self, player):
        if not self.picked and player.x == self.x and player.y == self.y:
            self.picked = True
            return True
        return False