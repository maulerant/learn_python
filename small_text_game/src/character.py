from random import randint, choice
from abc import abstractmethod

from small_text_game.src.event import KickEvent
from small_text_game.src.event_manager import EventManager
from small_text_game.src.options import *


class Character:
    directions = [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT]
    health = 0
    max_health = 0
    char = ''

    def __init__(self, name):
        self.name = name
        self.action = ''
        self.position = [-1, -1]
        self.direction = DIRECTION_UP
        self.heal = randint(1, MAX_HEAL)
        self.ap = randint(1, MAX_AP)
        EventManager.getInstance().bind(KickEvent.name, self, 'damage_deal_event')

    def cure(self):
        self.health = min(self.health + self.heal, self.max_health)

    def is_dead(self):
        return self.health <= 0

    def damage_deal_event(self, event):
        if event.position == self.position:
            self.damage_deal(int(event.data))

    def damage_deal(self, damage):
        self.health -= damage

    def get_action(self):
        return choice([ATTACK, HEAL])

    def get_char(self):
        return self.char

    def place_on(self, map):
        x, y = map.get_empty_random_position()
        self.position = [x, y]
        map.put(x, y, self.get_char())

    def get_position(self):
        return self.position

    def show_health(self):
        print(f"{self.name}`s hp = {self.health}")

    @abstractmethod
    def turn(self, map):
        pass

