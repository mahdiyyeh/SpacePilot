from AssetLoader import *
from Effect import Effect
from Spritesheet import Spritesheet
from Vector import Vector

EFFECT_SHEETS = {
    1 : load_image("plus-one.png"),
    2: load_image("plus-two.png"),
    3: load_image("plus-three.png")
}

# animation constants
EFFECT_FRAME_DURATION = 2
EFFECT_SHEET_COLUMNS = 16
EFFECT_SHEET_ROWS = 1
EFFECT_SPRITE_WIDTH = 32
EFFECT_SPRITE_HEIGHT = 32
EFFECT_FRAME_SIZES = ([(EFFECT_SPRITE_WIDTH, EFFECT_SPRITE_HEIGHT)] *
                       (EFFECT_SHEET_COLUMNS * EFFECT_SHEET_ROWS))

# inherits from Effect class due to similar methods, only difference is values of animation constants
class ScoreIndicator(Effect):
    def __init__(self, effect, pos):
        super().__init__(effect, pos)
        self.sprite = Spritesheet(
            EFFECT_SHEETS[effect],
            EFFECT_SHEET_COLUMNS,
            EFFECT_SHEET_ROWS,
            EFFECT_FRAME_SIZES,
            EFFECT_FRAME_DURATION)
        self.pos = Vector(pos.x, pos.y)
