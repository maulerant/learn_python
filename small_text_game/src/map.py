from random import randint

from small_text_game.src.options import *


class Map:
    delta_xy = {
        DIRECTION_UP: (0, -1),
        DIRECTION_DOWN: (0, 1),
        DIRECTION_LEFT: (-1, 0),
        DIRECTION_RIGHT: (1, 0),
    }

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
        return self.map[y][x] if self.is_valid_pos(x, y) else STONE

    def put(self, x, y, char):
        self.map[y][x] = char

    def get_max_quantity(self, quantity):
        count_empty_char = self.count(self.empty_char)
        return count_empty_char if count_empty_char < quantity else quantity

    def place(self, quantity, char):
        for i in range(self.get_max_quantity(quantity)):
            self._place_item_to_random_position(char)

    def get_empty_random_position(self):
        if self.count(self.empty_char) == 0:
            return -1, -1
        while True:
            x, y = randint(0, self.width - 1), randint(0, self.height - 1)
            if self.check(x, y, self.empty_char):
                break
        return x, y

    def _place_item_to_random_position(self, char):
        x, y = self.get_empty_random_position()
        self.put(x, y, char)

    def check(self, x, y, char):
        return self.map[y][x] == char

    def count(self, char):
        count = 0
        for y in range(0, self.height):
            count += self.map[y].count(char)
        return count


    def calculate_position(self, x, y, direction):
        return self.delta_xy[direction][0] + x, self.delta_xy[direction][1] + y

    def is_valid_pos(self, x, y):
        return self.height > y >= 0 and self.width > x >= 0

    def move(self, char, start_position, new_position):
        if self.is_valid_pos(new_position[0], new_position[1]):
            self.put(start_position[0], start_position[1], self.empty_char)
            self.put(new_position[0], new_position[1], char)

    def clear(self, position):
        self.put(position[0], position[1], self.empty_char)

    def size(self):
        return [self.width, self.height]

    def row(self, row):
        return self.map[row]
