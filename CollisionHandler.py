import Config
from ScoreIndicator import ScoreIndicator
from Explosion import Explosion
import math

from Vector import Vector


class CollisionHandler:
    def __init__(self, game = None):
        self.explosions = []
        self.effects = []
        self.game = game

    # calculate the distance between the centres of 2 objects using pythagoras' theorem
    def get_distance(self, object1, object2):
        x1, y1 = object1.pos.get_p()
        x2, y2 = object2.pos.get_p()

        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    def contact(self, object1, object2):
        distance = self.get_distance(object1, object2)
        return distance < (object1.radius + object2.radius)

    def check_collisions(self, player, enemy_manager):
        # use copy method to prevent errors when iterating over lists
        for bullet in player.bullets.copy():
            for enemy in enemy_manager.enemies.copy():
                if self.contact(bullet, enemy):
                    # check the objects still exist before trying to remove them to prevent errors
                    if bullet in player.bullets:
                        player.bullets.remove(bullet)
                    if enemy in enemy_manager.enemies:
                        enemy_manager.enemies.remove(enemy)
                    # create explosion and +(score) effect
                    self.explosions.append(Explosion(enemy.pos))
                    self.game.increase_score(enemy.size)
                    self.effects.append(ScoreIndicator(enemy.size, enemy.pos.add(Vector(16, 0))))

        # if enemy makes it to players side of screen
        for enemy in enemy_manager.enemies.copy():
            if enemy.pos.y > Config.CANVAS_HEIGHT:
                self.game.decrease_lives()
                if enemy in enemy_manager.enemies:
                    enemy_manager.enemies.remove(enemy)

        if enemy_manager.enemies == [] and enemy_manager.num_spawned == enemy_manager.max_enemies:
            self.game.increase_level()

        # handle collisions with player
        for bullet in enemy_manager.bullets.copy():
            if self.contact(bullet, player):
                if bullet in enemy_manager.bullets:
                    enemy_manager.bullets.remove(bullet)
                player.on_hit()

    def draw_explosions(self, canvas):
        for explosion in self.explosions:
            explosion.update(canvas)
            if explosion.exploded:
                if explosion in self.explosions:
                    self.explosions.remove(explosion)
        self.draw_effects(canvas)

    def draw_effects(self, canvas):
        for effect in self.effects:
            effect.update(canvas)
            if effect.finished:
                if effect in self.effects:
                    self.effects.remove(effect)
