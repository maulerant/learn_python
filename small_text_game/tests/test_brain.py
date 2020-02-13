import unittest
from random import randint
from unittest.mock import patch

from small_text_game.src.brain import *
from small_text_game.src.options import *


class BrainTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.position = [randint(0, 100), randint(0, 100)]

    def test_make_brain_object(self):
        brain = Brain()
        self.assertIsNotNone(brain)

    def test_generate_object_by_char(self):
        brain = Brain()
        self.assertIsInstance(brain.recognize(EMPTY, self.position), Empty)
        self.assertIsInstance(brain.recognize(TREE, self.position), Tree)
        self.assertIsInstance(brain.recognize(STONE, self.position), Stone)
        self.assertIsInstance(brain.recognize(LETTER, self.position), Letter)
        self.assertIsInstance(brain.recognize(TREASURE, self.position), Treasure)


    @patch('small_text_game.src.map.Map')
    def test_user_see(self, MockMap):
        x, y = randint(0, 100), randint(0, 100)
        brain = Brain()
        attrs = {'get.return_value': TREE, 'calculate_position.return_value': [x, y - 1]}
        MockMap.configure_mock(**attrs)
        self.assertEqual(brain.see(MockMap, [x, y], DIRECTION_UP), (TREE, [x, y - 1]))


if __name__ == '__main__':
    unittest.main()
