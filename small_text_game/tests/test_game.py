import unittest
from unittest.mock import patch

from small_text_game.src.game import Game, GameOverException
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

    @patch('small_text_game.src.map.Map')
    @patch('small_text_game.src.user.User')
    def test_game_turn(self, MockMap, MockUser):
        game = Game()
        game.map = MockMap
        game.user = MockUser
        game.turn()
        game.map.show.assert_called_once()
        # game.user.see.assert_called_once()


    @patch('small_text_game.src.map.Map')
    def test_game_turn_raise_exception_if_user_dead(self, MockMap):
        game = Game()
        game.map = MockMap

        game.user.health = 0
        with self.assertRaises(GameOverException):
            game.turn()

    @patch('small_text_game.src.map.Map')
    def test_game_turn_raise_exception_if_users_inventory_full(self, MockMap):
        game = Game()
        game.map = MockMap

        game.user.inventory[TREASURE] = MAX_TREASURES
        with self.assertRaises(GameOverException):
            game.turn()

    def test_game_not_over_if_user_live_and_inventory_empty(self):
        game = Game()
        self.assertFalse(game.user.is_dead())
        self.assertFalse(game.user.has(MAX_TREASURES, TREASURE))
        self.assertFalse(game.is_over())

    def test_game_is_over_if_user_dead(self):
        game = Game()
        game.user.health = 0
        self.assertTrue(game.user.is_dead())
        self.assertFalse(game.user.has(MAX_TREASURES, TREASURE))
        self.assertTrue(game.is_over())

    def test_game_is_over_if_inventory_full(self):
        game = Game()
        game.user.inventory[TREASURE] = MAX_TREASURES
        self.assertFalse(game.user.is_dead())
        self.assertTrue(game.user.has(MAX_TREASURES, TREASURE))
        self.assertTrue(game.is_over())


if __name__ == '__main__':
    unittest.main()
