from small_text_game.src.options import *


class Brain:
    def recognize(self, char):
        if char == TREE:
            return Tree()
        if char == STONE:
            return Stone()
        if char == LETTER:
            return Letter()
        if char == TREASURE:
            return Treasure()
        return Empty()


class Empty:
    def message(self):
        return 'Впереди пусто'

    def actions(self):
        return [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT]


class Tree:
    def message(self):
        return 'вы уперлись лбом в дерево'

    def actions(self):
        return [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, HACK]


class Stone:
    def message(self):
        return 'вы уперлись лбом в камень'

    def actions(self):
        return [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT]


class Letter:
    def message(self):
        return 'Вы видите письмо'

    def actions(self):
        return [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, READ]


class Treasure:
    def message(self):
        return 'Вы видите сокровище'

    def actions(self):
        return [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, PICK_UP]
