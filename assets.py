import pygame

class Assets:
    def __init__(self):
        self.player_img = pygame.image.load("assets/player.png")
        self.monster_img = pygame.image.load("assets/monster.png")
        self.item_img = pygame.image.load("assets/item.png")
        self.wall_img = pygame.image.load("assets/wall.png")
        self.floor_img = pygame.image.load("assets/floor.png")
    
    def get_player(self):
        return self.player_img
    
    def get_monster(self):
        return self.monster_img
    
    def get_item(self):
        return self.item_img
    
    def get_wall(self):
        return self.wall_img
    
    def get_floor(self):
        return self.floor_img