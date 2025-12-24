from Clock import Clock
from AssetLoader import *
from Spritesheet import Spritesheet
from Enemy import Enemy
from Vector import Vector
from Config import *

import random

# Load enemy sprite sheets
ENEMY_SMALL_SHEET = load_image("enemy-small.png")
ENEMY_MEDIUM_SHEET = load_image("enemy-medium.png")
ENEMY_BIG_SHEET = load_image("enemy-big.png")

# Define sprite dimensions
SPRITE1_WIDTH = 16
SPRITE1_HEIGHT = 16
SPRITE2_WIDTH = 32
SPRITE2_HEIGHT = 16
SPRITE3_WIDTH = 32
SPRITE3_HEIGHT = 32

# Animation properties
ENEMY_FRAME_DURATION = 5
SPRITE_COLUMNS = 2
SPRITE_ROWS = 1

# Define frame sizes for different enemy types
ENEMY_SMALL_FRAME_SIZES = ([(SPRITE1_WIDTH, SPRITE1_HEIGHT)] *
                           (SPRITE_COLUMNS * SPRITE_ROWS))
ENEMY_MEDIUM_FRAME_SIZES = ([(SPRITE2_WIDTH, SPRITE2_HEIGHT)] *
                           (SPRITE_COLUMNS * SPRITE_ROWS))
ENEMY_BIG_FRAME_SIZES = ([(SPRITE3_WIDTH, SPRITE3_HEIGHT)] *
                           (SPRITE_COLUMNS * SPRITE_ROWS))

# Maximum time interval for enemy spawning
MAX_SPAWN_RATE = 300

class EnemyManager:
    def __init__(self, game):
        # Initialize the enemy manager, responsible for handling enemy spawning and updates
        self.clock = Clock() 
        self.enemies = [] 
        self.bullets = []  
        self.num_spawned = 0  
        self.max_enemies = 4  
        self.spawn_interval = random.randint(1, MAX_SPAWN_RATE) 
        self.game = game  
        self.spawn_enemies(self.max_enemies) 

    def spawn_enemy(self):
        # Spawn a single enemy with a random size and position.
        size = random.choice([1, 2, 3])  # Randomly select enemy size
        
        # Assign appropriate sprite sheet based on size
        if size == 1:
            sprite_sheet = Spritesheet(ENEMY_SMALL_SHEET, SPRITE_COLUMNS,
                                       SPRITE_ROWS, ENEMY_SMALL_FRAME_SIZES, ENEMY_FRAME_DURATION)
        elif size == 2:
            sprite_sheet = Spritesheet(ENEMY_MEDIUM_SHEET, SPRITE_COLUMNS,
                                       SPRITE_ROWS, ENEMY_MEDIUM_FRAME_SIZES, ENEMY_FRAME_DURATION)
        else:
            sprite_sheet = Spritesheet(ENEMY_BIG_SHEET, SPRITE_COLUMNS,
                                       SPRITE_ROWS, ENEMY_BIG_FRAME_SIZES, ENEMY_FRAME_DURATION)

        # Generate random x-position within screen bounds
        x = random.randint(50, CANVAS_WIDTH - 50)
        y = -50  # Spawn enemy just above the visible screen
        
        # Create and store the enemy
        enemy = Enemy(sprite_sheet, Vector(x, y), size, self)
        self.enemies.append(enemy)
        
        # Adjust spawn interval based on game level
        self.spawn_interval = random.randint(1, int(MAX_SPAWN_RATE / (self.game.level * 0.35)))

    def spawn_enemies(self, num):
        # Spawn a set number of enemies at the start of the game or level
        self.num_spawned = 0
        self.max_enemies = num
        self.spawn_enemy()  

    def update(self, canvas):
        # Update enemies and bullets, handle spawning logic
        self.clock.tick()  
        self.update_enemies(canvas)  
        
        # Update bullets and draw them on canvas
        for bullet in self.bullets:
            bullet.update(canvas)

        # Spawn new enemy if time interval is met and max limit not reached
        if self.clock.transition(self.spawn_interval) and self.num_spawned < self.max_enemies:
            self.spawn_enemy()
            self.num_spawned += 1

    def update_enemies(self, canvas):
        # Update all active enemies and render them on the screen
        for enemy in self.enemies:
            enemy.update(canvas)

    def reset(self):
        # Reset enemy manager, clearing all enemies and bullets 
        self.enemies.clear()  
        self.bullets.clear()  
        self.num_spawned = 0  
        self.clock.time = 0  

