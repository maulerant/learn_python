import unittest
from random import choice, randint

from small_text_game.src.game import Game
from small_text_game.src.map import Map
from small_text_game.src.options import EMPTY


class GameTestCase(unittest.TestCase):
    def test_make_game_object(self):
        game = Game()
        self.assertIsNotNone(game)

    def test_init_map(self):
        game = Game()
        game.generate_map(20, 10, EMPTY)
        self.assertIsNotNone(game.map)
        self.assertIsInstance(game.map, Map)


if __name__ == '__main__':
    unittest.main()
