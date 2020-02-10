from small_text_game.src.options import *


class User:
    def __init__(self, name):
        self.direction = DIRECTION_UP
        self.health = MAX_USER_HEALTH
        self.inventory = []
        self.name = name
        self.position = [-1, -1]

    def get_position(self):
        return self.position

    def has(self, quantity, char):
        return self.inventory.count(char) == quantity

    def to_inventory(self, char):
        self.inventory.append(char)

    def is_dead(self):
        return self.health <= 0

    def see(self, map):
        return map.get_in_direction(self.position[0], self.position[1], self.direction)

    def place_on_map(self, map):
        pass

