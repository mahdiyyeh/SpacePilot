from Spritesheet import Spritesheet
from Vector import Vector

# constants for spritesheet
POWERUP_FRAME_DURATION = 6
POWERUP_SHEET_COLUMNS = 2
POWERUP_SHEET_ROWS = 1
POWERUP_SPRITE_WIDTH = 16
POWERUP_SPRITE_HEIGHT = 16
POWERUP_FRAME_SIZES = ([(POWERUP_SPRITE_WIDTH, POWERUP_SPRITE_HEIGHT)] *
                       (POWERUP_SHEET_COLUMNS * POWERUP_SHEET_ROWS))

class Powerup:
    def __init__(self, effect, pos, img):
        # type of effect
        self.effect = effect
        self.pos = pos
        self.velocity = Vector(0, 2)
        self.sprite = Spritesheet(
            img,
            POWERUP_SHEET_COLUMNS,
            POWERUP_SHEET_ROWS,
            POWERUP_FRAME_SIZES,
            POWERUP_FRAME_DURATION)
        # make radius minimum to prevent unusual collisions
        self.radius = min(POWERUP_SPRITE_WIDTH, POWERUP_SPRITE_HEIGHT)

    def update(self, canvas):
        self.sprite.draw(canvas, self.pos)
        self.pos.add(self.velocity)
