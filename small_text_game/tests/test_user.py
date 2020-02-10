import unittest
from unittest.mock import patch

from small_text_game.src.user import User
from small_text_game.src.options import *


class UserTestCase(unittest.TestCase):
    def test_make_user_object(self):
        user = User('Name')
        self.assertIsNotNone(user)
        self.assertEqual(user.name, 'Name')

    def test_user_has_inventory(self):
        user = User('Name')
        self.assertIsInstance(user.inventory, list)
        self.assertEqual(len(user.inventory), 0)

    def test_user_has_health(self):
        user = User('Name')
        self.assertEqual(user.health, MAX_USER_HEALTH)

    def test_get_user_default_position(self):
        user = User('Name')
        position = user.get_position()
        self.assertIsInstance(position, list)
        self.assertEqual(len(position), 2)
        self.assertEqual(position, [-1, -1])
        self.assertEqual(user.direction, DIRECTION_UP)

    def test_user_put_item_to_inventory(self):
        user = User('Name')
        self.assertEqual(user.inventory.count(TREASURE), 0)
        user.to_inventory(TREASURE)
        self.assertEqual(user.inventory.count(TREASURE), 1)

    def test_user_has_items(self):
        user = User('Name')
        self.assertTrue(user.has(0, TREASURE))
        self.assertEqual(user.inventory.count(TREASURE), 0)

        self.assertFalse(user.has(1, TREASURE))
        user.to_inventory(TREASURE)
        self.assertTrue(user.has(1, TREASURE))

    def test_user_is_dead(self):
        user = User('User')
        self.assertFalse(user.is_dead())

        user.health = 0
        self.assertTrue(user.is_dead())

        user.health = -1
        self.assertTrue(user.is_dead())

    @patch('small_text_game.src.map.Map')
    def test_user_see(self, MockMap):
        user = User('User')
        attrs = {'get_in_direction.return_value': TREE}
        MockMap.configure_mock(**attrs)
        self.assertEqual(user.see(MockMap), TREE)

    @patch('small_text_game.src.map.Map')
    def test_place_on_map(self, MockMap):
        user = User('User')
        attrs = {'get_empty_random_position.return_value': (1, 1)}
        MockMap.configure_mock(**attrs)
        user.place_on_map(MockMap)
        self.assertEqual(user.position, (1, 1))


if __name__ == '__main__':
    unittest.main()
