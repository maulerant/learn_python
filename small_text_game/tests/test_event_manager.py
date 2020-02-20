import unittest
from random import randint
from unittest.mock import patch

from small_text_game.src.event import *
from small_text_game.src.event_manager import EventManager
from small_text_game.src.monster import Monster


class EventManagerTestCase(unittest.TestCase):
    def test_create_event_manager_object(self):
        event_manager = EventManager()
        self.assertNotEqual(event_manager, EventManager.getInstance())

    def test_make_event_manager_instance(self):
        event_manager = EventManager.getInstance()
        self.assertIsNotNone(event_manager)
        self.assertEqual(event_manager, EventManager.getInstance())
        self.assertEqual(event_manager._instance, event_manager)

    def test_subscriptions_dict(self):
        event_manager = EventManager()
        self.assertIsNone(event_manager.subscribers)

        event_manager = EventManager.getInstance()
        self.assertIsInstance(event_manager.subscribers, dict)

    @patch('small_text_game.src.user.User')
    def test_bind_subscriber_to_event(self, MockUser):
        event_manger = EventManager.getInstance()
        self.assertEqual(event_manger.subscribers, {})
        callback = 'damage_deal'
        event_manger.bind(KickEvent.name, MockUser, callback)
        self.assertEqual(event_manger.subscribers, {KickEvent.name: [{'object': MockUser, 'callback': callback}]})

        event_manger.bind(KickEvent.name, MockUser, callback)
        self.assertEqual(event_manger.subscribers, {KickEvent.name: [{'object': MockUser, 'callback': callback}]})

        event_manger.bind(Event.name, MockUser, callback)
        self.assertEqual(event_manger.subscribers, {
            KickEvent.name: [{'object': MockUser, 'callback': callback}],
            Event.name: [{'object': MockUser, 'callback': callback}]
        })

        monster = Monster('Ork')
        event_manger.bind(Event.name, monster, callback)
        self.assertEqual(event_manger.subscribers, {
            KickEvent.name: [{'object': MockUser, 'callback': callback}],
            Event.name: [
                {'object': MockUser, 'callback': callback},
                {'object': monster, 'callback': callback},
            ]
        })

    @patch('small_text_game.src.user.User')
    def test_unbind_subscriber_to_event(self, MockUser):
        event_manager = EventManager.getInstance()
        event_manager.subscribers = {}
        callback = 'damage_deal'
        event_manager.bind(KickEvent.name, MockUser, callback)
        self.assertEqual(event_manager.subscribers, {KickEvent.name: [{'object': MockUser, 'callback': callback}]})

        event_manager.unbind(KickEvent.name, MockUser, '')
        self.assertEqual(event_manager.subscribers, {KickEvent.name: [{'object': MockUser, 'callback': callback}]})

        event_manager.unbind(KickEvent.name, MockUser, callback)
        self.assertEqual(event_manager.subscribers, {KickEvent.name: []})

    @patch('small_text_game.src.user.User')
    def test_dispatch_events(self, MockUser):
        event_manger = EventManager.getInstance()
        event_manger.subscribers = {}
        position = [randint(0, 100), randint(0, 100)]

        MockUser.position = position
        event_manger.bind(KickEvent.name, MockUser, 'damage_deal')

        damage = randint(1, 100)
        event = KickEvent(position, damage)
        event_manger.dispatch(event)
        MockUser.damage_deal.assert_called_with(event)

    def test_object_is_event(self):
        self.assertTrue(EventManager.getInstance().is_event(KickEvent([], 0)))
        self.assertFalse(EventManager.getInstance().is_event({}))
        self.assertFalse(EventManager.getInstance().is_event(10))


if __name__ == '__main__':
    unittest.main()
