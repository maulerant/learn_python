import unittest
from unittest.mock import patch
from random import randint
from small_text_game.src.knowledge import *


class KnowledgeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.position = [randint(0, 100), randint(0, 100)]

    def test_empty_object(self):
        object = Empty(self.position)
        self.assertEqual(object.position, self.position)
        self.assertIsInstance(object, KnowledgeAbout)
        self.assertEqual(object.message(), 'Впереди пусто')
        self.assertEqual(object.can_do(), [])
        self.assertFalse(object.it_barier())

    def test_tree_object(self):
        object = Tree(self.position)
        self.assertIsInstance(object, KnowledgeAbout)
        self.assertEqual(object.position, self.position)
        self.assertEqual(object.message(), 'вы уперлись лбом в дерево')
        self.assertEqual(object.can_do(), [HACK])
        self.assertTrue(object.it_barier())

    def test_stone_object(self):
        object = Stone(self.position)
        self.assertIsInstance(object, KnowledgeAbout)
        self.assertEqual(object.position, self.position)
        self.assertEqual(object.message(), 'вы уперлись лбом в камень')
        self.assertEqual(object.can_do(), [])
        self.assertTrue(object.it_barier())

    def test_letter_object(self):
        object = Letter(self.position)
        self.assertIsInstance(object, KnowledgeAbout)
        self.assertEqual(object.position, self.position)
        self.assertEqual(object.message(), 'Вы видите письмо')
        self.assertEqual(object.can_do(), [READ])
        self.assertTrue(object.it_barier())
        self.assertIsNotNone(object.info)

    def test_treasure_object(self):
        object = Treasure(self.position)
        self.assertIsInstance(object, KnowledgeAbout)
        self.assertEqual(object.position, self.position)
        self.assertEqual(object.message(), 'Вы видите сокровище')
        self.assertEqual(object.can_do(), [PICK_UP])
        self.assertTrue(object.it_barier())

    def test_monster_object(self):
        object = Monster(self.position)
        self.assertIsInstance(object, KnowledgeAbout)
        self.assertEqual(object.position, self.position)
        self.assertEqual(object.message(), 'Перед Вами злой монстр')
        self.assertEqual(object.can_do(), [ATTACK, HEAL])
        self.assertTrue(object.it_barier())

    @patch('small_text_game.src.user.User')
    @patch('small_text_game.src.map.Map')
    def test_tree_do_action(self, map, user):
        tree = Tree(self.position)
        tree.do(user, HACK, map)
        map.clear.assert_called_with(self.position)

    @patch('small_text_game.src.user.User')
    @patch('small_text_game.src.map.Map')
    def test_tree_do_action(self, map, user):
        treasure = Treasure(self.position)
        treasure.do(user, HACK, map)
        map.clear.assert_called_with(self.position)
        user.to_inventory.assert_called_with(TREASURE)

    @patch('small_text_game.src.user.User')
    @patch('small_text_game.src.map.Map')
    def test_tree_do_action(self, map, user):
        letter = Letter(self.position)
        letter.do(user, HACK, map)
        map.clear.assert_called_with(self.position)
        user.to_inventory.assert_called_with(LETTER)
        user.new_message.assert_called_with(letter.info)

    @unittest.skip('моки для синглтона')
    @patch('small_text_game.src.event_manager.EventManager')
    @patch('small_text_game.src.user.User')
    @patch('small_text_game.src.map.Map')
    def test_monster_do_action(self, map, user, event_manager):
        monster = Monster(self.position)
        monster.do(user, HEAL, map)
        user.cure.assert_called_once()

        event_manager.getInstance.return_value = event_manager
        monster.do(user, ATTACK, map)
        event_manager.getInstance.assert_called_once()


if __name__ == '__main__':
    unittest.main()
