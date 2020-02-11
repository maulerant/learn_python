import unittest

from small_text_game.src.brain import *
from small_text_game.src.options import *


class BrainTestCase(unittest.TestCase):
    def test_make_brain_object(self):
        brain = Brain()
        self.assertIsNotNone(brain)

    def test_generate_object_by_char(self):
        brain = Brain()
        self.assertIsInstance(brain.recognize(EMPTY), Empty)
        self.assertIsInstance(brain.recognize(TREE), Tree)
        self.assertIsInstance(brain.recognize(STONE), Stone)
        self.assertIsInstance(brain.recognize(LETTER), Letter)
        self.assertIsInstance(brain.recognize(TREASURE), Treasure)

    def test_empty_object(self):
        empty = Empty()
        self.assertEqual(empty.message(), 'Впереди пусто')
        self.assertEqual(empty.actions(), [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT])

    def test_tree_object(self):
        tree = Tree()
        self.assertEqual(tree.message(), 'вы уперлись лбом в дерево')
        self.assertEqual(tree.actions(), [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, HACK])


    def test_stone_object(self):
        object = Stone()
        self.assertEqual(object.message(), 'вы уперлись лбом в камень')
        self.assertEqual(object.actions(), [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT])

    def test_letter_object(self):
        object = Letter()
        self.assertEqual(object.message(), 'Вы видите письмо')
        self.assertEqual(object.actions(), [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, READ])

    def test_treasure_object(self):
        object = Treasure()
        self.assertEqual(object.message(), 'Вы видите сокровище')
        self.assertEqual(object.actions(), [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, PICK_UP])

if __name__ == '__main__':
    unittest.main()
