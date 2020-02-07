from small_text_game.src.map import Map


class Game:
    def __init__(self):
        self.map = Map()

    def generate_map(self, width, height, empty_char):
        self.map.generate(width, height, empty_char)