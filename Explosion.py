from AssetLoader import *
from Clock import Clock
from Spritesheet import Spritesheet

EXPLOSION_SHEET = load_image("explosion.png")
EXPLOSION_SOUND = load_sound("explosion.wav")

# constants for spritesheet
EXPLOSION_FRAME_DURATION = 6
EXPLOSION_SHEET_COLUMNS = 6
EXPLOSION_SHEET_ROWS = 1
EXPLOSION_SPRITE_WIDTH = 32
EXPLOSION_SPRITE_HEIGHT = 32
EXPLOSION_FRAME_SIZES = ([(EXPLOSION_SPRITE_WIDTH, EXPLOSION_SPRITE_HEIGHT)] *
                         (EXPLOSION_SHEET_ROWS * EXPLOSION_SHEET_COLUMNS))

class Explosion:
    def __init__(self, pos):
        self.clock = Clock()
        self.pos = pos
        self.exploded = False
        self.sprite = Spritesheet(
            EXPLOSION_SHEET,
            EXPLOSION_SHEET_COLUMNS,
            EXPLOSION_SHEET_ROWS,
            EXPLOSION_FRAME_SIZES,
            EXPLOSION_FRAME_DURATION)
        EXPLOSION_SOUND.play()

    def update(self, canvas):
        # mark as finished once animation reaches final frame
        if self.sprite.frame_index == EXPLOSION_SHEET_COLUMNS - 1:
            self.exploded = True
        if not self.exploded:
            self.sprite.draw(canvas, self.pos)
