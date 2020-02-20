import unittest
from random import randint
from unittest.mock import patch

from small_text_game.src.character import Character
from small_text_game.src.monster import Monster
from small_text_game.src.map import Map
from small_text_game.src.options import *


class MonsterTestCase(unittest.TestCase):
    def test_make_monster_object(self):
        monster = Monster('Ork')
        self.assertIsNotNone(monster)
        self.assertIsInstance(monster, Character)
        self.assertEqual(monster.health, MAX_MONSTER_HEALTH)
        self.assertEqual(monster.max_health, MAX_MONSTER_HEALTH)
        self.assertEqual(monster.char, MONSTER)

    @patch('small_text_game.src.map.Map')
    def test_not_find_enemy(self, MockMap):
        monster = Monster('Ork')
        MockMap.get.return_value = EMPTY
        self.assertFalse(monster.find_enemy(MockMap))
        self.assertEqual(MockMap.get.call_count, 4)
        self.assertEqual(MockMap.calculate_position.call_count, 4)

    @patch('small_text_game.src.map.Map')
    def test_find_enemy(self, MockMap):
        monster = Monster('Ork')
        monster.direction = DIRECTION_LEFT
        MockMap.get.return_value = USER
        self.assertTrue(monster.find_enemy(MockMap))
        self.assertEqual(monster.direction, monster.directions[0])
        MockMap.calculate_position.assert_called_once()
        MockMap.get.assert_called_once()

    @patch('small_text_game.src.map.Map')
    def test_get_enemy_postion(self, MockMap):
        monster = Monster('Ork')
        position = (randint(1, 10), randint(1, 10))
        MockMap.calculate_position.return_value = position
        self.assertEqual(monster.enemy_position(MockMap), [position[0], position[1]])

    @patch('small_text_game.src.map.Map')
    def test_killed(self, MockMap):
        monster = Monster('Ork')
        monster.killed(MockMap)
        MockMap.clear.assert_called_with(monster.position)


if __name__ == '__main__':
    unittest.main()
