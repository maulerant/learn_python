from small_text_game.src.options import *
from small_text_game.src.brain import Brain


class User:
    directions = [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT]

    def __init__(self, name):
        self.messages = []
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

    def place_on(self, map):
        x, y = map.get_empty_random_position()
        self.position = [x, y]
        map.put(x, y, USER)

    def turn(self, map):
        self.show_messages()
        print("В Вашем инвентаре %d сокровищ" % self.inventory.count(TREASURE))
        print(f"Смотрим в направлении {self.direction}")
        knowledge_about = self.brain.knowledge(map, self.position, self.direction)
        print(knowledge_about.message())
        direction = ','.join(self.can_walk_to(self.direction, knowledge_about))
        self.action = input(
            f"Идти в направлении [{direction}] или [{'.'.join(knowledge_about.can_do())}]: ")
        self.do(map, knowledge_about)

    def can_walk_to(self, direction, knowledge_about):
        directions = self.directions.copy()
        if knowledge_about.it_barier():
            directions.remove(direction)
        return directions

    def do(self, map, knowledge_about):
        if self.action in self.directions:
            self.move(self.action, map)
        if self.action in knowledge_about.can_do():
            knowledge_about.do(self, self.action, map)

    def move(self, action, map):
        self.direction = action
        knowledge_about = self.brain.knowledge(map, self.position, self.direction)
        if not knowledge_about.it_barier():
            map.move(USER, self.position, knowledge_about.position)
            self.position = knowledge_about.position

    def new_message(self, text):
        self.messages.append(text)

    def show_messages(self):
        while len(self.messages) > 0:
            print(self.messages.pop())
