from small_text_game.src.map import Map
from small_text_game.src.user import User


class Game:
    def __init__(self):
        self.map = Map()
        self.user = User('Name')

    def generate_map(self, width, height, empty_char):
        self.map.generate(width, height, empty_char)

    def place_on_map(self, quantity, char):
        self.map.place(quantity, char)
