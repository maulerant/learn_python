"""
текстовая игра
генерируются два объекта игрок и монстр,
здоровье и сила атаки рандомные
ходят по очереди
у каждого есть два варианта действия "атака" и "лечиться"
за монстра играет компьютер. выбор действия: рандомно
побеждает выживший
"""

from random import randint

ACTION_ATTACK = 1
ACTION_HEAL = 2

MAX_USER_HP = randint(700, 900)
MAX_MONSTER_HP = randint(700, 900)


class Character:
    name = ''
    hp = 0
    heal = 0
    ap = 0
    max_hp = 0

    def show_hp(self):
        print(f"{self.name}`s hp = {self.hp}")

    def turn(self, enemy):
        character_action = self.get_action()
        if character_action == ACTION_ATTACK:
            enemy.damage_deal(self.ap)
        else:
            self.hp = min(self.hp + self.heal, self.max_hp)

    def is_dead(self):
        return self.hp <= 0

    def get_action(self):
        return randint(ACTION_ATTACK, ACTION_HEAL)

    def damage_deal(self, damage):
        self.hp -= damage


class User(Character):
    def __init__(self, name):
        self.name = name
        self.hp = MAX_USER_HP
        self.heal = randint(20, 90)
        self.ap = randint(20, 90)
        self.max_hp = MAX_USER_HP

    def get_action(self):
        user_action = int(input(f"select attack {ACTION_ATTACK} or heal {ACTION_HEAL}: "))
        while user_action not in (ACTION_ATTACK, ACTION_HEAL):
            print('not available action')
            user_action = int(input(f"select attack {ACTION_ATTACK} or heal {ACTION_HEAL}: "))

        return user_action


class Monster(Character):
    def __init__(self, name):
        self.name = name
        self.hp = MAX_MONSTER_HP
        self.heal = randint(20, 90)
        self.ap = randint(20, 90)
        self.max_hp = MAX_MONSTER_HP


monster = Monster('Ork')
user = User('User')

while True:
    monster.show_hp()
    user.show_hp()

    user.turn(monster)
    if monster.is_dead():
        print('user win')
        break

    monster.turn(user)
    if user.is_dead():
        print('user lose')
        break
