import Config
from Clock import Clock
from CollisionHandler import CollisionHandler
from GameState import GameState
from AssetLoader import *
from Player import Player
from EnemyManager import EnemyManager
from PowerupManager import PowerupManager
from Vector import Vector
from Sound import *


try:
     import simplegui
except ImportError:
     import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

START_BG = load_image("start-bg.png")
IN_GAME_BG = load_image("in-game-bg.png")
GAME_OVER_BG = load_image("game-over-bg.png")


BUTTON_SOUND = load_sound("button.wav")
LEVEL_UP_SOUND = load_sound("level-up.wav")

PLAYER_SPEED = 6


class Game:
    def __init__(self):
        self.state = GameState.START
        self.score = 0
        self.level = 1
        self.button_option = 0
        self.level_change_timer = Clock()
        self.player = None
        self.enemy_manager = None
        self.powerup_manager = None
        self.collision_handler = CollisionHandler(self)

    def start_game(self):
        # initialising player, enemies, powerups and collision handler  
        self.state = GameState.IN_GAME
        self.score = 0
        self.level = 1
        self.player = Player(self)
        self.enemy_manager = EnemyManager(self)
        self.powerup_manager = PowerupManager()

    def exit_game(self):
        sound.stop_music()
        frame.stop()

    def game_over(self):
        self.state = GameState.GAME_OVER

    def help_page(self):
        self.state = GameState.HELP

    def back_button_handler(self):
        self.state = GameState.START

    def increase_level(self):
        self.state = GameState.CHANGE_LEVEL
        LEVEL_UP_SOUND.play()
        self.level += 1
        self.player.bullets.clear()
        self.enemy_manager.reset()
        self.enemy_manager.spawn_enemies(int(self.level * 2.5) + 3)

    def increase_score(self, score):
        self.score += score

    def decrease_lives(self):
        if self.player.lives > 0:
            self.player.lives -= 1
        if self.player.lives == 0:
            self.game_over()

    def restart(self):
        # resets player, enemies, and powerups 
        self.enemy_manager = EnemyManager(self)
        self.player = Player(self)
        self.powerup_manager = PowerupManager()
        self.start_game()

    def update_game(self, canvas):
        # main game loop which updates player, enemies, powerups 
        self.player.update(canvas)
        self.enemy_manager.update(canvas)
        self.collision_handler.check_collisions(self.player, self.enemy_manager)
        self.collision_handler.draw_explosions(canvas)
        self.powerup_manager.update(canvas, self.player)

    def draw(self, canvas):
        # canvas is updated based on game state 
        if self.state == GameState.START:
            self.draw_start(canvas)
        elif self.state == GameState.IN_GAME:
            self.draw_bg(canvas)
            self.update_game(canvas)
            self.draw_stats(canvas)
        elif self.state == GameState.HELP:
            self.draw_help(canvas)
        elif self.state == GameState.GAME_OVER:
            self.draw_game_over(canvas)
        elif self.state == GameState.CHANGE_LEVEL:
            self.level_change_timer.tick()
            self.draw_bg(canvas)
            self.draw_stats(canvas)
            self.draw_level(canvas)
            if self.level_change_timer.transition(240):
                self.state = GameState.IN_GAME

    def draw_start(self, canvas):
        canvas.draw_image(
            START_BG,
            (START_BG.get_width() / 2, START_BG.get_height() / 2),
            (START_BG.get_width(), START_BG.get_height()),
            (Config.CANVAS_WIDTH / 2, Config.CANVAS_WIDTH / 2),
            (Config.CANVAS_WIDTH, Config.CANVAS_HEIGHT))

        canvas.draw_text("START", (200, 200), 60, "White", "monospace")
        canvas.draw_text("HELP", (200, 300), 60, "White", "monospace")
        canvas.draw_text("EXIT", (200, 400), 60, "White", "monospace")

        if self.button_option == 0:
            canvas.draw_text("START", (200, 200), 60, "aqua", "monospace")
            canvas.draw_text(">      <", (140, 200), 60, "aqua", "monospace")
        if self.button_option == 1:
            canvas.draw_text("HELP", (200, 300), 60, "aqua", "monospace")
            canvas.draw_text(">     <", (140, 300), 60, "aqua", "monospace")
        if self.button_option == 2:
            canvas.draw_text("EXIT", (200, 400), 60, "aqua", "monospace")
            canvas.draw_text(">     <", (140, 400), 60, "aqua", "monospace")

    def draw_stats(self,canvas):
        canvas.draw_text(f"Level {self.level}", (20, 30), 25, "White", "monospace")
        canvas.draw_text(f"Score: {self.score}", (20, 60), 25, "White", "monospace")
        canvas.draw_text(f"Lives: {self.player.lives}", (20, 90), 25, "White", "monospace")

    def draw_bg(self, canvas):
        canvas.draw_image(
            IN_GAME_BG,
            (IN_GAME_BG.get_width() / 2, IN_GAME_BG.get_height() / 2),
            (IN_GAME_BG.get_width(), IN_GAME_BG.get_height()),
            (Config.CANVAS_WIDTH / 2, Config.CANVAS_WIDTH / 2),
            (Config.CANVAS_WIDTH, Config.CANVAS_HEIGHT))

    def draw_help(self, canvas):
        # game rules 
        canvas.draw_text("BACK TO MENU [M]", (30, 30), 25, "aqua", "monospace")

        canvas.draw_text("> Use the arrow keys to move ", (50, 100), 25, "Red", "monospace")
        canvas.draw_text("> Use the spacebar to shoot", (50, 125), 25, "Red", "monospace")
        canvas.draw_text("> Destroy enemies to increase your", (50, 150), 25, "Red", "monospace")
        canvas.draw_text("  score", (50, 175), 25, "Red", "monospace")
        canvas.draw_text("> Destroy all enemies to level up", (50, 200), 25, "Red", "monospace")
        canvas.draw_text("> There are 3 power ups available:", (50, 225), 25, "Red", "monospace")
        canvas.draw_text("    -> +1 life (green powerup)", (50, 250), 25, "Red", "monospace")
        canvas.draw_text("    -> faster shooting (red power up)", (50, 275), 25, "Red", "monospace")
        canvas.draw_text("    -> shield (blue power up)", (50, 300), 25, "Red", "monospace")
        canvas.draw_text("> As your level increases, the", (50, 325), 25, "Red", "monospace")
        canvas.draw_text("  number of enemies will increase", (50, 350), 25, "Red", "monospace")
        canvas.draw_text("> Taking damage by enemies or", (50, 375), 25, "Red", "monospace")
        canvas.draw_text("  letting them escape will decreases your lives", (50, 400), 25, "Red", "monospace")
        canvas.draw_text("  your lives", (50, 425), 25, "Red", "monospace")
        canvas.draw_text("> Once all lives are lost, game over", (50, 450), 25, "Red", "monospace")

    def draw_game_over(self, canvas):
        canvas.draw_image(
            GAME_OVER_BG,
            (GAME_OVER_BG.get_width() / 2, GAME_OVER_BG.get_height() / 2),
            (GAME_OVER_BG.get_width(), GAME_OVER_BG.get_height()),
            (Config.CANVAS_WIDTH / 2, Config.CANVAS_WIDTH / 2),
            (Config.CANVAS_WIDTH, Config.CANVAS_HEIGHT))

        canvas.draw_text("GAME OVER!", (140, 100), 60, "white", "monospace")
        canvas.draw_text(f"Score: {self.score}", (220, 175), 45, "white", "monospace")
        canvas.draw_text(f"Level: {self.level}", (220, 225), 45, "white", "monospace")
        canvas.draw_text("Restart [R]", (175, 425), 40, "White", "monospace")
        canvas.draw_text("Main Menu [M]", (150, 475), 40, "White", "monospace")
        canvas.draw_text("Exit [E]", (220, 525), 40, "White", "monospace")

    def draw_level(self, canvas):
        canvas.draw_text(f"> LEVEL {self.level} <", (130, 300), 50, "White", "monospace")

    def key_down_handler(self, key):
        if self.state == GameState.START:
            if key == simplegui.KEY_MAP['down']:
                self.button_option += 1
                BUTTON_SOUND.play()
                if self.button_option > 2:
                    self.button_option = 0
            if key == simplegui.KEY_MAP['up']:
                BUTTON_SOUND.play()
                self.button_option -= 1
                if self.button_option < 0:
                    self.button_option = 2
            self.button_option = max(0, min(2, self.button_option))
            if key == simplegui.KEY_MAP['space']:
                BUTTON_SOUND.play()
                if self.button_option == 0:
                    self.start_game()
                elif self.button_option == 1:
                    self.help_page()
                elif self.button_option == 2:
                    self.exit_game()
        elif self.state == GameState.HELP:
            if key == simplegui.KEY_MAP['m']:
                BUTTON_SOUND.play()
                self.back_button_handler()
        elif self.state == GameState.GAME_OVER:
            if key == simplegui.KEY_MAP["r"]:
                BUTTON_SOUND.play()
                self.restart()
            elif key == simplegui.KEY_MAP["m"]:
                BUTTON_SOUND.play()
                self.state = GameState.START
            elif key == simplegui.KEY_MAP["e"]:
                BUTTON_SOUND.play()
                self.exit_game()
        elif self.state == GameState.IN_GAME or self.state == GameState.CHANGE_LEVEL: # key handler for player
            if key == simplegui.KEY_MAP["left"]:
                self.player.velocity.add(Vector(-PLAYER_SPEED, 0))
            if key == simplegui.KEY_MAP["right"]:
                self.player.velocity.add(Vector(PLAYER_SPEED, 0))
            if key == simplegui.KEY_MAP["up"]:
                self.player.velocity.add(Vector(0, -PLAYER_SPEED))
            if key == simplegui.KEY_MAP["down"]:
                self.player.velocity.add(Vector(0, PLAYER_SPEED))
            if key == simplegui.KEY_MAP["space"]:
                self.player.shooting = True

    def key_up_handler(self, key):
        if self.state == GameState.IN_GAME or self.state == GameState.CHANGE_LEVEL:
            if key == simplegui.KEY_MAP["left"]:
                self.player.velocity.subtract(Vector(-PLAYER_SPEED, 0))
            if key == simplegui.KEY_MAP["right"]:
                self.player.velocity.subtract(Vector(PLAYER_SPEED, 0))
            if key == simplegui.KEY_MAP["up"]:
                self.player.velocity.subtract(Vector(0, -PLAYER_SPEED))
            if key == simplegui.KEY_MAP["down"]:
                self.player.velocity.subtract(Vector(0, PLAYER_SPEED))
            if key == simplegui.KEY_MAP["space"]:
                self.player.shooting = False

game = Game()
sound.play_music()

frame = simplegui.create_frame("Space Invaders", Config.CANVAS_WIDTH, Config.CANVAS_HEIGHT, 0)
frame.set_draw_handler(game.draw)
frame.set_keydown_handler(game.key_down_handler)
frame.set_keyup_handler(game.key_up_handler)

frame.start()
