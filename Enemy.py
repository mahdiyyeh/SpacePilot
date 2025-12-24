import random
from Bullet import Bullet
from AssetLoader import *

# Load shooting sound effect
SHOOT_SOUND = load_sound("shoot.wav")

class Enemy:
    def __init__(self, sprite_sheet, pos, size, enemy_manager):
        self.spritesheet = sprite_sheet
        self.enemy_manager = enemy_manager
        self.pos = pos
        self.size = size
        self.radius = 64  # Defines the enemy's collision radius

        # Determines how often the enemy shoots (smaller enemies shoot less often)
        self.shoot_interval = random.randint(100, 200) // size  
        self.shoot_timer = 0 

    def update(self, canvas):
        # Moves the enemy down, checks if it should shoot, and redraws it
        self.pos.y += self.size / 3.5  # Larger enemies move faster
        self.shoot_timer += 1 

        self.draw(canvas) 

        # If the timer reaches the shoot interval, fire a bullet
        if self.shoot_timer >= self.shoot_interval:
            self.shoot()
            self.shoot_timer = 0  

    def shoot(self):
        # Fires a bullet from the enemy's position
        SHOOT_SOUND.rewind() 
        SHOOT_SOUND.play()  

        bullet = Bullet(self.pos, False)  
        self.enemy_manager.bullets.append(bullet)  

    def draw(self, canvas):
        # Draws the enemy using its sprite sheet
        self.spritesheet.draw(canvas, self.pos)
