import unittest
from unittest.mock import patch

from small_text_game.src.camera import Camera
from small_text_game.src.event import MessageEvent
from small_text_game.src.game import Game, GameOverException
from small_text_game.src.map import Map
from small_text_game.src.options import *
from small_text_game.src.user import User


class GameTestCase(unittest.TestCase):
    def test_make_game_object(self):
        game = Game()
        self.assertIsNotNone(game)
        self.assertIsInstance(game.user, User)
        self.assertIsInstance(game.camera, Camera)
        self.assertIsInstance(game.monsters, list)
        self.assertEqual(len(game.monsters), MAX_MONSTERS)

    def test_init_map(self):
        game = Game()
        self.assertIsNotNone(game.map)
        self.assertIsInstance(game.map, Map)
        self.assertIsInstance(game.messages, list)
        self.assertEqual(len(game.messages), 0)

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

    @patch('small_text_game.src.monster.Monster')
    @patch('small_text_game.src.camera.Camera')
    @patch('small_text_game.src.user.User')
    def test_game_turn(self, MockUser, MockCamera, MockMonster):
        game = Game()
        game.camera = MockCamera
        game.user = MockUser
        MockMonster.is_dead.return_value = False
        game.monsters = [
            MockMonster
        ]
        attrs = {'is_dead.return_value': False, 'has.return_value': False}
        game.user.configure_mock(**attrs)
        game.turn()
        game.camera.show.assert_called_with(game.map, game.user, SMOG_RADIUS)
        game.user.turn.assert_called_with(game.map)
        MockMonster.turn.assert_called_with(game.map)

    @patch('small_text_game.src.camera.Camera')
    @patch('small_text_game.src.user.User')
    def test_game_turn_raise_exception_if_user_dead(self, MockUser, MockCamera):
        game = Game()
        game.camera = MockCamera
        game.user = MockUser
        attrs = {'is_dead.return_value': True, 'has.return_value': False}
        game.user.configure_mock(**attrs)

        with self.assertRaises(GameOverException):
            game.turn()

    @patch('small_text_game.src.camera.Camera')
    @patch('small_text_game.src.user.User')
    def test_game_turn_raise_exception_if_users_inventory_full(self, MockUser, MockCamera):
        game = Game()
        game.camera = MockCamera
        game.user = MockUser
        attrs = {'is_dead.return_value': False, 'has.return_value': True}
        game.user.configure_mock(**attrs)

        with self.assertRaises(GameOverException):
            game.turn()

    @patch('small_text_game.src.user.User')
    def test_game_not_over_if_user_live_and_inventory_empty(self, MockUser):
        game = Game()
        game.user = MockUser
        attrs = {'is_dead.return_value': False, 'has.return_value': False}
        game.user.configure_mock(**attrs)
        self.assertFalse(game.is_over())

    @patch('small_text_game.src.user.User')
    def test_game_is_over_if_user_dead(self, MockUser):
        game = Game()
        game.user = MockUser
        attrs = {'is_dead.return_value': True, 'has.return_value': False}
        game.user.configure_mock(**attrs)
        self.assertTrue(game.is_over())

    @patch('small_text_game.src.user.User')
    def test_game_is_over_if_inventory_full(self, MockUser):
        game = Game()
        game.user = MockUser
        attrs = {'is_dead.return_value': False, 'has.return_value': True}
        game.user.configure_mock(**attrs)
        self.assertTrue(game.is_over())

    def test_new_message_event(self):
        game = Game()
        self.assertEqual(len(game.messages), 0)
        message = 'lorem ipsum'
        game.new_message(MessageEvent(None, message))
        self.assertEqual(len(game.messages), 1)
        self.assertIn(message, game.messages)

        message = ['lorem ipsum2']
        game.new_message(MessageEvent(None, message))
        self.assertEqual(len(game.messages), 2)
        self.assertIn(message[0], game.messages)


if __name__ == '__main__':
    unittest.main()
