from small_text_game.src.options import *


class User:
    def __init__(self, name):
        self.health = MAX_USER_HEALTH
        self.inventory = {
            TREASURE: 0
        }
        self.name = name
        self.position = [-1, -1]

    def get_position(self):
        return self.position

    def has(self, quantity, char):
        return self.inventory[char] == quantity

    def to_inventory(self, char):
        self.inventory[char] += 1

    def is_dead(self):
        return self.health <= 0
