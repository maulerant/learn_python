from small_text_game.src.character import Character
from small_text_game.src.event import *
from small_text_game.src.event_manager import EventManager

from small_text_game.src.options import *


class Monster(Character):
    def __init__(self, name):
        super().__init__(name)

        self.health = MAX_MONSTER_HEALTH
        self.max_health = MAX_MONSTER_HEALTH
        self.char = MONSTER

    def turn(self, map):
        if self.find_enemy(map):
            messages = []
            self.action = self.get_action()
            if self.action == ATTACK:
                EventManager.getInstance().dispatch(KickEvent(self.enemy_position(map), self.ap))
                messages.append(f'{self.name} kick {self.ap}')
            else:
                self.cure()
                messages.append(f'{self.name} heal {self.heal}')
            EventManager.getInstance().dispatch(MessageEvent(None, messages))

    def find_enemy(self, map):
        for direction in self.directions:
            position = map.calculate_position(self.position[0], self.position[1], direction)
            if map.get(position[0], position[1]) == USER:
                self.direction = direction
                return True
        return False

    def enemy_position(self, map):
        position = map.calculate_position(self.position[0], self.position[1], self.direction)
        return [position[0], position[1]]

    def killed(self, map):
        map.clear(self.position)
        EventManager.getInstance().unbind(KickEvent.name, self, 'damage_deal_event')
