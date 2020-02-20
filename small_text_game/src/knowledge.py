from abc import ABC, abstractmethod
from random import choice

from small_text_game.src.event import KickEvent, MessageEvent
from small_text_game.src.event_manager import EventManager
from small_text_game.src.options import *


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
        map.clear(self.position)

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
    def __init__(self, position):
        super(Letter, self).__init__(position)
        self.info = f'В письме написано: {choice(INFOS)}'

    def do(self, user, action, map):
        map.clear(self.position)
        user.to_inventory(LETTER)
        user.new_message(self.info)

    def message(self):
        return 'Вы видите письмо'

    def can_do(self):
        return [READ]


class Treasure(KnowledgeAbout):
    def do(self, user, action, map):
        map.clear(self.position)
        user.to_inventory(TREASURE)

    def message(self):
        return 'Вы видите сокровище'

    def can_do(self):
        return [PICK_UP]


class Monster(KnowledgeAbout):
    def do(self, user, action, map):
        messages = []
        if action == HEAL:
            user.cure()
            messages.append(f'{user.name} heal {user.heal}')
        if action == ATTACK:
            EventManager.getInstance().dispatch(KickEvent(self.position, user.ap))
            messages.append(f'{user.name} kick {user.ap}')
        EventManager.getInstance().dispatch(MessageEvent(None, messages))

    def message(self):
        return 'Перед Вами злой монстр'

    def can_do(self):
        return [ATTACK, HEAL]
