from Vector import Vector
from Clock import Clock
from AssetLoader import *
from Powerup import Powerup
from PowerupEffect import PowerupEffect
from CollisionHandler import CollisionHandler
from Effect import Effect

import Config
import random

POWERUP_SHEETS = {
    PowerupEffect.FIRE_RATE : "powerup-one.png",
    PowerupEffect.SHIELD : "powerup-two.png",
    PowerupEffect.HEALTH : "powerup-three.png"
}
POWERUP_SOUND = load_sound("powerup.wav")

MAX_SPAWN_RATE = 1600
POWERUP_DURATION = 360

class PowerupManager:
    def __init__(self):
        self.collision_handler = CollisionHandler()
        self.clock = Clock()
        # timers to make sure powerups expire
        self.shield_timer = Clock()
        self.firerate_timer = Clock()
        self.powerups = []
        # effects to indicate a powerup has been collected
        self.effects = []
        self.spawn_interval = random.randint(1, MAX_SPAWN_RATE)

    def spawn_powerup(self):
        effect = random.choice([
            PowerupEffect.FIRE_RATE,
            PowerupEffect.SHIELD,
            PowerupEffect.HEALTH])
        img = load_image(POWERUP_SHEETS[effect])

        x = random.randint(0, Config.CANVAS_WIDTH)
        y = 0

        powerup = Powerup(effect, Vector(x, y), img)

        self.powerups.append(powerup)
        # randomise spawn interval
        self.spawn_interval = random.randint(1, MAX_SPAWN_RATE)
        self.clock.time = 0

    def update(self, canvas, player):
        self.clock.tick()
        self.firerate_timer.tick()
        self.shield_timer.tick()
        self.update_powerups(canvas, player)
        self.draw_effects(canvas)

        if self.clock.transition(self.spawn_interval):
            self.spawn_powerup()

    def update_powerups(self, canvas, player):
        for powerup in self.powerups:
            powerup.update(canvas)

            if self.collision_handler.contact(powerup, player):
                POWERUP_SOUND.play()
                # create new pickup effect and add to list
                self.effects.append(Effect(powerup.effect, player.pos))
                self.apply_effect(powerup, player)
                self.powerups.remove(powerup)

        # method is called every frame so check expiry here
        self.check_expiry(player)

    def draw_effects(self, canvas):
        for effect in self.effects:
            effect.update(canvas)
            if effect.finished:
                if effect in self.effects:
                    self.effects.remove(effect)

    def check_expiry(self, player):
        if self.firerate_timer.time >= POWERUP_DURATION:
            player.remove_effect(PowerupEffect.FIRE_RATE)
            self.firerate_timer.time = 0

        if self.shield_timer.time >= POWERUP_DURATION:
            player.remove_effect(PowerupEffect.SHIELD)
            self.shield_timer.time = 0

    def apply_effect(self, powerup, player):
        if powerup.effect == PowerupEffect.FIRE_RATE:
            self.firerate_timer.time = 0
        elif powerup.effect == PowerupEffect.SHIELD:
            self.shield_timer.time = 0

        player.apply_effect(powerup)
