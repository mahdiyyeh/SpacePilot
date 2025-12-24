from AssetLoader import *
from Spritesheet import Spritesheet
from PowerupEffect import PowerupEffect
from Clock import Clock
from Vector import Vector

EFFECT_SHEETS = {
    PowerupEffect.FIRE_RATE : load_image("effect-one.png"),
    PowerupEffect.SHIELD : load_image("effect-two.png"),
    PowerupEffect.HEALTH : load_image("effect-three.png"),
    1 : load_image("plus-one.png"),
    2: load_image("plus-two.png"),
    3: load_image("plus-three.png")
}

# constants for sprite animation
EFFECT_FRAME_DURATION = 4
EFFECT_SHEET_COLUMNS = 8
EFFECT_SHEET_ROWS = 1
EFFECT_SPRITE_WIDTH = 32
EFFECT_SPRITE_HEIGHT = 32
EFFECT_FRAME_SIZES = ([(EFFECT_SPRITE_WIDTH, EFFECT_SPRITE_HEIGHT)] *
                       (EFFECT_SHEET_COLUMNS * EFFECT_SHEET_ROWS))

class Effect:
    def __init__(self, effect, pos):
        self.sprite = Spritesheet(
            EFFECT_SHEETS[effect],
            EFFECT_SHEET_COLUMNS,
            EFFECT_SHEET_ROWS,
            EFFECT_FRAME_SIZES,
            EFFECT_FRAME_DURATION)
        self.clock = Clock()
        self.pos = pos
        self.finished = False

    def update(self, canvas):
        # if the animation has reached the end then mark as finished
        if self.sprite.frame_index == self.sprite.columns - 1:
            self.finished = True
        if not self.finished:
            self.sprite.draw(canvas, self.pos)
