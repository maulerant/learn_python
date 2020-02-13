from small_text_game.src.knowledge import *
from small_text_game.src.options import *


class Brain:
    def knowledge(self, map, current_position, direction):
        char, position = self.see(map, current_position, direction)
        return self.recognize(char, position)

    def recognize(self, char, position):
        if char in objects.keys():
            return globals()[objects[char]](position)
        return Empty(position)

    def see(self, map, position, direction):
        new_x, new_y = map.calculate_position(position[0], position[1], direction)
        return map.get(new_x, new_y), [new_x, new_y]


