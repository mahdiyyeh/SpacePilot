import Config
from AssetLoader import *
from Vector import Vector
from Spritesheet import Spritesheet

BULLET_FRAME_DURATION = 5
BULLET_SHEET_COLUMNS = 1
BULLET_SHEET_ROWS = 2
BULLET_SPRITE_WIDTH = 6
BULLET_SPRITE_HEIGHT = 19
BULLET_FRAME_SIZES = ([(BULLET_SPRITE_WIDTH, BULLET_SPRITE_HEIGHT)] *
                      (BULLET_SHEET_COLUMNS * BULLET_SHEET_ROWS))

PLAYER_BULLET_SHEET = load_image("player-bullet.png")
ENEMY_BULLET_SHEET = load_image("enemy-bullet.png")

BULLET_SPEED = 6

class Bullet:
    def __init__(self, pos, player_bullet):
        self.pos = Vector(pos.x, pos.y)
        self.velocity = Vector(0, -BULLET_SPEED)
        self.sprite = Spritesheet(
            PLAYER_BULLET_SHEET,
            BULLET_SHEET_COLUMNS,
            BULLET_SHEET_ROWS,
            BULLET_FRAME_SIZES,
            BULLET_FRAME_DURATION)
        self.radius = min(BULLET_SPRITE_WIDTH, BULLET_SPRITE_HEIGHT)

        if not player_bullet:
            self.velocity = Vector(0, BULLET_SPEED)
            self.sprite.img = ENEMY_BULLET_SHEET

    def update(self, canvas):
        self.pos.add(self.velocity)
        self.draw(canvas)

    def draw(self, canvas):
        self.sprite.draw(canvas, self.pos)

    def on_screen(self):
        return 0 <= self.pos.y <= Config.CANVAS_HEIGHT