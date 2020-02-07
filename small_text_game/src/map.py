from random import randint

from small_text_game.src.options import EMPTY


class Map:
    def __init__(self):
        self.map = []
        self.width = 0
        self.height = 0
        self.empty_char = ''

    def generate(self, width, height, empty_char):
        self.map = [[empty_char for x in range(width)] for y in range(height)]
        self.width = width
        self.height = height
        self.empty_char = empty_char

    def get(self, x, y):
        return self.map[y][x]

    def put(self, x, y, char):
        self.map[y][x] = char

    def place(self, quantity, char):
        for i in range(quantity):
            while True:
                x, y = randint(0, self.width - 1), randint(0, self.height - 1)
                if self.check(x, y, self.empty_char):
                    self.put(x, y, char)
                    break

    def check(self, x, y, char):
        return self.map[y][x] == char

    def count(self, char):
        count = 0
        for y in range(0, self.height):
            for x in range(0, self.width):
                count += 1 if self.map[y][x] == char else 0
        return count
