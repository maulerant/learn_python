import unittest
from unittest.mock import patch

from small_text_game.src.game import Game
from small_text_game.src.map import Map
from small_text_game.src.options import *
from small_text_game.src.user import User


class GameTestCase(unittest.TestCase):
    def test_make_game_object(self):
        game = Game()
        self.assertIsNotNone(game)
        self.assertIsInstance(game.user, User)

    def test_init_map(self):
        game = Game()
        self.assertIsNotNone(game.map)
        self.assertIsInstance(game.map, Map)

    @patch('small_text_game.src.map.Map')
    def test_map_generation(self, MockMap):
        game = Game()
        game.map = MockMap
        game.generate_map(20, 10, EMPTY)
        game.map.generate.assert_called_with(20, 10, EMPTY)

    @patch('small_text_game.src.map.Map')
    def test_place_items_on_map(self, MockMap):
        game = Game()
        game.map = MockMap
        game.generate_map(20, 10, EMPTY)
        game.place_on_map(20, TREE)
        game.map.place.assert_called_with(20, TREE)


if __name__ == '__main__':
    unittest.main()
