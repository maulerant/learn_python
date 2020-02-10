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

    def get_max_quantity(self, quantity):
        count_empty_char = self.count(self.empty_char)
        return count_empty_char if count_empty_char < quantity else quantity

    def place(self, quantity, char):
        for i in range(self.get_max_quantity(quantity)):
            self._place_item_to_random_position(char)

    def _place_item_to_random_position(self, char):
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
            count += self.map[y].count(char)
        return count

    def show(self):
        print('-' * self.width)
        for y in range(self.height):
            print(''.join(self.map[y]))
        print('-' * self.width)
