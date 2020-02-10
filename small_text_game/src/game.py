from small_text_game.src.map import Map
from small_text_game.src.user import User
from small_text_game.src.options import *


class GameOverException(Exception):
    pass


class Game:
    def __init__(self):
        self.map = Map()
        self.user = User('Name')

    def generate_map(self, width, height, empty_char):
        self.map.generate(width, height, empty_char)

    def place_on_map(self, quantity, char):
        self.map.place(quantity, char)

    def run(self):
        while True:
            self.turn()

    def turn(self):
        self.map.show()
        if self.is_over():
            raise GameOverException()

    def is_over(self):
        return self.user.is_dead() or self.user.has(MAX_TREASURES, TREASURE)
