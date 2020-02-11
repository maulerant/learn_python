from small_text_game.src.options import *
from small_text_game.src.brain import Brain


class User:
    def __init__(self, name):
        self.brain = Brain()
        self.direction = DIRECTION_UP
        self.health = MAX_USER_HEALTH
        self.inventory = []
        self.name = name
        self.position = [-1, -1]
        self.action = ''

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

    def place_on(self, map):
        x, y = map.get_empty_random_position()
        self.position = [x, y]
        map.put(x, y, USER)

    def show_info(self, map):
        print("В Вашем инвентаре %d сокровищ" % self.inventory.count(TREASURE))
        print(f"Смотрим в направлении {self.direction}")
        can_do = self.can_do_action(self.see(map))
        print(can_do['message'])
        self.action = input(f"{can_do['actions']}: ")

    def can_do_action(self, char):
        recognized_object = self.brain.recognize(char)
        return {
            'message': recognized_object.message(),
            'actions': recognized_object.actions()
        }
