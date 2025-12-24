from enum import Enum

class GameState(Enum):
    START = 1
    HELP = 2
    IN_GAME = 3
    CHANGE_LEVEL = 4
    GAME_OVER = 5