import unittest

from small_text_game.src.user import User
from small_text_game.src.options import *


class UserTestCase(unittest.TestCase):
    def test_make_user_object(self):
        user = User('Name')
        self.assertIsNotNone(user)
        self.assertEqual(user.name, 'Name')

    def test_user_has_inventory(self):
        user = User('Name')
        self.assertIsInstance(user.inventory, dict)

    def test_user_has_health(self):
        user = User('Name')
        self.assertEqual(user.health, MAX_USER_HEALTH)

    def test_get_user_default_position(self):
        user = User('Name')
        position = user.get_position()
        self.assertIsInstance(position, list)
        self.assertEqual(len(position), 2)
        self.assertEqual(position, [-1, -1])

    def test_user_put_item_to_inventory(self):
        user = User('Name')
        self.assertEqual(user.inventory[TREASURE], 0)
        user.to_inventory(TREASURE)
        self.assertEqual(user.inventory[TREASURE], 1)

    def test_user_has_items(self):
        user = User('Name')
        self.assertTrue(user.has(0, TREASURE))
        self.assertEqual(user.inventory[TREASURE], 0)

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


if __name__ == '__main__':
    unittest.main()
