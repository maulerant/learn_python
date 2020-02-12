import unittest
from unittest.mock import patch
from random import choice, randint

from small_text_game.src.map import Map
from small_text_game.src.options import *


class MapTestCase(unittest.TestCase):
    def test_make_map(self):
        map = Map()
        self.assertIsNotNone(map)
        self.assertIsNotNone(map.map)
        self.assertIsInstance(map.map, list)
        self.assertEqual(map.width, 0)
        self.assertEqual(map.height, 0)
        self.assertEqual(map.empty_char, '')

    def test_init_map(self):
        width = 20
        height = 10
        map = Map()
        map.generate(width, height, EMPTY)
        self.assertEqual(height, len(map.map))
        self.assertEqual(width, len(choice(map.map)))
        self.assertEqual(EMPTY, map.get(randint(0, width - 1), randint(0, height - 1)))
        self.assertEqual(map.width, width)
        self.assertEqual(map.height, height)
        self.assertEqual(map.empty_char, EMPTY)

        width = 2
        height = 5
        map.generate(width, height, TREE)
        self.assertEqual(TREE, map.get(randint(0, width - 1), randint(0, height - 1)))
        self.assertEqual(map.width, width)
        self.assertEqual(map.height, height)
        self.assertEqual(map.empty_char, TREE)

    def test_get_item_by_xy(self):
        map = Map()
        map.generate(20, 10, EMPTY)
        self.assertEqual(map.get(-1, -1), STONE)
        self.assertEqual(map.get(1, 1), EMPTY)

    def test_is_valid_pos(self):
        map = Map()
        map.generate(20, 10, EMPTY)
        self.assertFalse(map.is_valid_pos(-1, -1))
        self.assertTrue(map.is_valid_pos(1, 1))

    def test_put_item_on_map(self):
        x, y = randint(0, 20 - 1), randint(0, 10 - 1)
        map = Map()
        map.generate(20, 10, EMPTY)

        self.assertEqual(EMPTY, map.get(x, y))
        map.put(x, y, TREE)
        self.assertEqual(TREE, map.get(x, y))

    def test_check_if_position_contain_char(self):
        map = Map()
        map.generate(20, 10, TREE)
        map.put(10, 5, EMPTY)
        self.assertTrue(map.check(10, 5, EMPTY))
        self.assertFalse(map.check(10, 6, EMPTY))
        self.assertTrue(map.check(10, 6, TREE))

    def test_calculate_items_on_map(self):
        map = Map()
        map.generate(20, 10, EMPTY)
        count = 0
        for x, y in [[0, 0], [3, 4], [5, 6]]:
            count += 1
            map.put(x, y, TREE)

        self.assertEqual(map.count(TREE), count)
        self.assertEqual(map.count(EMPTY), 20 * 10 - count)

    def test_place_items_on_map(self):
        map = Map()
        map.generate(20, 10, EMPTY)
        map.place(20, TREE)
        self.assertEqual(map.count(TREE), 20)

    def test_get_max_quantity_of_chars(self):
        width, height = 10, 10
        map = Map()
        map.generate(width, height, EMPTY)
        self.assertEqual(map.get_max_quantity(1), 1)
        self.assertEqual(map.get_max_quantity(width * height), width * height)
        self.assertEqual(map.get_max_quantity(width * height + 1), width * height)

    def test_calculate_position_by_xy_and_direction(self):
        map = Map()
        self.assertEqual(map.calculate_position(1, 1, DIRECTION_UP), (1, 0))
        self.assertEqual(map.calculate_position(1, 1, DIRECTION_DOWN), (1, 2))
        self.assertEqual(map.calculate_position(1, 1, DIRECTION_LEFT), (0, 1))
        self.assertEqual(map.calculate_position(1, 1, DIRECTION_RIGHT), (2, 1))

    @patch('small_text_game.src.map.randint')
    def test_get_empty_random_position(self, mocked_randint):
        map = Map()
        map.generate(20, 20, EMPTY)
        random_value = randint(1, 10)
        mocked_randint.return_value = random_value
        self.assertEqual(map.get_empty_random_position(), (random_value, random_value))

        map.generate(20, 20, TREE)
        map.empty_char = EMPTY
        self.assertEqual(map.get_empty_random_position(), (-1, -1))


if __name__ == '__main__':
    unittest.main()
