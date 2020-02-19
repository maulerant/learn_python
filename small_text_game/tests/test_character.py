import sys
import unittest
from random import randint
from unittest.mock import patch

from small_text_game.src.character import Character
from small_text_game.src.map import Map
from small_text_game.src.options import *


class CharacterTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.name = 'Name'
        self.character = Character(self.name)

    def test_make_character_object(self):
        self.assertIsNotNone(self.character)
        self.assertEqual(self.character.name, self.name)
        self.assertEqual(self.character.health, 0)
        self.assertIsNot(self.character.heal, 0)
        self.assertIsNot(self.character.ap, 0)
        self.assertEqual(self.character.max_health, 0)
        self.assertEqual(self.character.char, '')
        self.assertEqual(self.character.action, '')

    def test_get_character_default_position(self):
        position = self.character.get_position()
        self.assertIsInstance(position, list)
        self.assertEqual(len(position), 2)
        self.assertEqual(position, [-1, -1])
        self.assertEqual(self.character.direction, DIRECTION_UP)
        self.assertEqual(self.character.directions, [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT])

    def test_damage_deal(self):
        self.character.health = 0
        damage = 100
        self.character.damage_deal(damage)
        self.assertEqual(self.character.health, -100)

        damage = 200
        self.character.damage_deal(damage)
        self.assertEqual(self.character.health, -300)

    def test_cure(self):
        self.character.max_health = sys.maxsize
        self.character.health = 0
        self.character.heal = randint(1, 100)
        self.character.cure()
        self.assertEqual(self.character.health, self.character.heal)
        self.character.cure()
        self.assertEqual(self.character.health, 2 * self.character.heal)

    def test_is_dead(self):
        self.character.health = 0
        self.assertTrue(self.character.is_dead())

        self.character.health = randint(1, 100)
        self.assertFalse(self.character.is_dead())

    def test_get_action(self):
        self.assertIn(self.character.get_action(), [ATTACK, HEAL])
        self.assertIn(self.character.get_action(), [ATTACK, HEAL])
        self.assertIn(self.character.get_action(), [ATTACK, HEAL])

    def test_get_char(self):
        self.character.char = MONSTER
        self.assertEqual(self.character.get_char(), MONSTER)
        self.character.char = USER
        self.assertEqual(self.character.get_char(), USER)

    @patch('small_text_game.src.map.Map')
    def test_place_on_map(self, MockMap):
        x, y = randint(0, 10), randint(0, 20)
        self.character.char = USER
        attrs = {'get_empty_random_position.return_value': (x, y)}
        MockMap.configure_mock(**attrs)
        self.character.place_on(MockMap)
        self.assertEqual(self.character.position, [x, y])
        MockMap.put.assert_called_with(x, y, USER)


if __name__ == '__main__':
    unittest.main()
