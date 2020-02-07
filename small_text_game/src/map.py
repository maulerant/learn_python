from small_text_game.src.options import EMPTY


class Map:
    def __init__(self):
        self.map = []

    def generate(self, width, height, empty_char):
        self.map = [[empty_char for x in range(width)] for y in range(height)]

    def get(self, x, y):
        return self.map[y][x]

    def put(self, x, y, char):
        pass