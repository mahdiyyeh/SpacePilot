import Config
from AssetLoader import *
from Bullet import Bullet
from Clock import Clock
from PowerupEffect import PowerupEffect
from Spritesheet import Spritesheet
from Vector import Vector

#load assets
PLAYER_SHEET = load_image("player.png")
SHOOT_SOUND = load_sound("shoot.wav")
SHIELD_SHEET = load_image("shield.png")

#player sprite settings
PLAYER_FRAME_DURATION = 5
PLAYER_SHEET_COLUMNS = 5
PLAYER_SHEET_ROWS = 2
PLAYER_SPRITE_WIDTH = 16
PLAYER_SPRITE_HEIGHT = 24
PLAYER_FRAME_SIZES = [(PLAYER_SPRITE_WIDTH, PLAYER_SPRITE_HEIGHT)] * (PLAYER_SHEET_COLUMNS * PLAYER_SHEET_ROWS)

#shield settings
SHIELD_SPRITE_WIDTH = 32
SHIELD_SPRITE_HEIGHT = 32

#shooting cooldown
PLAYER_BULLET_COOLDOWN = 20

class Player:
    def __init__(self, game):
        self.lives = 3  #player starts with 3 lives
        self.pos = Vector(Config.CANVAS_WIDTH / 2, Config.CANVAS_HEIGHT / 2)  #start at center
        self.velocity = Vector(0, 0)
        self.cooldown_timer = Clock()
        self.bullet_cooldown = PLAYER_BULLET_COOLDOWN
        self.bullets = []
        self.can_shoot = True
        self.shooting = False
        self.shield_active = False
        self.firerate_boosted = False
        self.sprite = Spritesheet(PLAYER_SHEET, PLAYER_SHEET_COLUMNS, PLAYER_SHEET_ROWS, PLAYER_FRAME_SIZES, PLAYER_FRAME_DURATION)
        self.radius = min(PLAYER_SPRITE_WIDTH, PLAYER_SPRITE_HEIGHT)
        self.game = game

    def move(self):
        self.pos.add(self.velocity)  #apply movement
        #keep player within screen bounds
        self.pos.x = max(0, min(Config.CANVAS_WIDTH, self.pos.x))
        self.pos.y = max(0, min(Config.CANVAS_HEIGHT, self.pos.y))

    def shoot(self):
        if self.can_shoot and self.shooting:
            SHOOT_SOUND.rewind()
            SHOOT_SOUND.play()
            self.bullets.append(Bullet(self.pos, True))  #spawn a bullet
            self.can_shoot = False

    def update(self, canvas):
        self.move()
        self.cooldown_timer.tick()
        if self.cooldown_timer.transition(self.bullet_cooldown):
            self.can_shoot = True  #reset shooting ability
        self.shoot()
        self.draw(canvas)
        
        #remove bullets that go off screen
        for bullet in self.bullets:
            if not bullet.on_screen():
                if bullet:
                    self.bullets.remove(bullet)
            bullet.update(canvas)

    def draw(self, canvas):
        self.sprite.draw(canvas, self.pos)
        if self.shield_active:
            self.draw_shield(canvas)

    def draw_shield(self, canvas):
        #draw shield at player's position
        canvas.draw_image(SHIELD_SHEET, (SHIELD_SPRITE_WIDTH / 2, SHIELD_SPRITE_HEIGHT / 2),
                          (SHIELD_SPRITE_WIDTH, SHIELD_SPRITE_HEIGHT), self.pos.get_p(),
                          (SHIELD_SPRITE_WIDTH * 2, SHIELD_SPRITE_HEIGHT * 2))

    def apply_effect(self, powerup):
        #apply power up effects
        if powerup.effect == PowerupEffect.FIRE_RATE:
            self.bullet_cooldown /= 2
            self.firerate_boosted = True
        elif powerup.effect == PowerupEffect.SHIELD:
            self.shield_active = True
        elif powerup.effect == PowerupEffect.HEALTH:
            self.lives += 1

    def remove_effect(self, powerup_type):
        #remove power up effects when expired
        if powerup_type == PowerupEffect.FIRE_RATE and self.firerate_boosted:
            self.bullet_cooldown *= 2
            self.firerate_boosted = False
        elif powerup_type == PowerupEffect.SHIELD and self.shield_active:
            self.shield_active = False

    def on_hit(self):
        #reduce life if not shielded
        if not self.shield_active:
            self.game.decrease_lives()
        self.shield_active = False
