import unittest

from small_text_game.src.user import User


class UserTestCase(unittest.TestCase):
    def test_make_user_object(self):
        user = User('Name')
        self.assertIsNotNone(user)
        self.assertEqual(user.name, 'Name')

    def test_get_user_position(self):
        user = User('Name')
        position = user.get_position()
        self.assertIsInstance(position, list)
        self.assertEqual(len(position), 2)
        self.assertEqual(position, (-1, -1))

if __name__ == '__main__':
    unittest.main()
