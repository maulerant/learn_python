from abc import ABC, abstractmethod

from small_text_game.src.options import *


class Brain:
    def knowledge(self, map, current_position, direction):
        char, position = self.see(map, current_position, direction)
        return self.recognize(char, position)

    def recognize(self, char, position):
        if char == TREE:
            return Tree(position)
        if char == STONE:
            return Stone(position)
        if char == LETTER:
            return Letter(position)
        if char == TREASURE:
            return Treasure(position)
        return Empty(position)

    def see(self, map, position, direction):
        new_x, new_y = map.calculate_position(position[0], position[1], direction)
        return map.get(new_x, new_y), [new_x, new_y]


class KnowledgeAbout(ABC):
    def __init__(self, position):
        self.position = position

    @abstractmethod
    def message(self):
        pass

    @abstractmethod
    def can_do(self):
        pass

    @abstractmethod
    def do(self, user, action, map):
        pass

    def it_barier(self):
        return True


class Empty(KnowledgeAbout):
    def do(self, user, action, map):
        pass

    def message(self):
        return 'Впереди пусто'

    def can_do(self):
        return []

    def it_barier(self):
        return False


class Tree(KnowledgeAbout):
    def do(self, user, action, map):
        pass

    def message(self):
        return 'вы уперлись лбом в дерево'

    def can_do(self):
        return [HACK]


class Stone(KnowledgeAbout):
    def do(self, user, action, map):
        pass

    def message(self):
        return 'вы уперлись лбом в камень'

    def can_do(self):
        return []


class Letter(KnowledgeAbout):
    def do(self, user, action, map):
        pass

    def message(self):
        return 'Вы видите письмо'

    def can_do(self):
        return [READ]


class Treasure(KnowledgeAbout):
    def do(self, user, action, map):
        pass

    def message(self):
        return 'Вы видите сокровище'

    def can_do(self):
        return [PICK_UP]
