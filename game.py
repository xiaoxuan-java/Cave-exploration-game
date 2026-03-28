import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from dungeon_generator import DungeonGenerator
from assets import Assets
from player import Player
from monster import Monster
from item import Item
import random

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.assets = Assets()
        self.clock = pygame.time.Clock()
        self.dungeon = DungeonGenerator(25, 18)
        self.map = self.dungeon.map
        
        # 获取所有可走的地板格子
        floor_tiles = [(x, y) for y, row in enumerate(self.map)
                              for x, cell in enumerate(row) if cell == 0]
        random.shuffle(floor_tiles)
        
        # 依次分配玩家、怪物、道具的位置，避免重叠
        positions = iter(floor_tiles)
        
        # 玩家初始位置
        px, py = next(positions)
        self.player = Player(px, py, self.assets.get_player())
        
        # 怪物
        self.monsters = []
        for _ in range(2):
            mx, my = next(positions)
            self.monsters.append(Monster(mx, my, self.assets.get_monster()))
        
        # 道具
        self.items = []
        for _ in range(2):
            ix, iy = next(positions)
            self.items.append(Item(ix, iy, self.assets.get_item()))
    
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
