import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from dungeon_generator import DungeonGenerator
from assets import Assets
from player import Player
from monster import Monster
from item import Item

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.assets = Assets()
        self.clock = pygame.time.Clock()
        self.dungeon = DungeonGenerator(25, 18)
        self.map = self.dungeon.map
        self.player = Player(1, 1, self.assets.get_player())
        self.monsters = [
            Monster(10, 10, self.assets.get_monster()),
            Monster(20, 5, self.assets.get_monster())
        ]
        self.items = [
            Item(5, 5, self.assets.get_item()),
            Item(15, 15, self.assets.get_item())
        ]
    
    def draw_map(self):
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                img = self.assets.get_floor() if cell == 0 else self.assets.get_wall()
                self.screen.blit(img, (x * 32, y * 32))
    
    def draw(self):
        self.draw_map()
        for item in self.items:
            item.draw(self.screen)
        for monster in self.monsters:
            monster.draw(self.screen)
        self.player.draw(self.screen)
    
    def handle_player_move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.player.move(0, -1, self.map)
            elif event.key == pygame.K_s:
                self.player.move(0, 1, self.map)
            elif event.key == pygame.K_a:
                self.player.move(-1, 0, self.map)
            elif event.key == pygame.K_d:
                self.player.move(1, 0, self.map)
    
    def handle_items(self):
        for item in self.items:
            item.try_pick(self.player)
    
    def monsters_act(self):
        for monster in self.monsters:
            monster.move_ai(self.player, self.map)
    
    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_player_move(event)
            
            self.monsters_act()
            self.handle_items()
            
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()