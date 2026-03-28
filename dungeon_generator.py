import random

class DungeonGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = self.generate_map()
        
    def generate_map(self):
        # Cellular Automata 随机洞穴生成
        chance_to_start_alive = 0.43
        death_limit = 3
        birth_limit = 4
        steps = 4
        
        map_data = [[1 if random.random() < chance_to_start_alive else 0 for _ in range(self.width)]
                    for _ in range(self.height)]
        
        for _ in range(steps):
            map_data = self.do_simulation_step(map_data, death_limit, birth_limit)
        return map_data
    
    def do_simulation_step(self, map_data, death_limit, birth_limit):
        new_map = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                alive_neighbors = self.count_alive_neighbors(map_data, x, y)
                if map_data[y][x] == 1:
                    if alive_neighbors < death_limit:
                        new_map[y][x] = 0
                    else:
                        new_map[y][x] = 1
                else:
                    if alive_neighbors > birth_limit:
                        new_map[y][x] = 1
                    else:
                        new_map[y][x] = 0
        return new_map
    
    def count_alive_neighbors(self, map_data, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = x + j, y + i
                if not (i == 0 and j == 0):
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        count += map_data[ny][nx]
                    else:
                        count += 1  # 边界外全是墙
        return count