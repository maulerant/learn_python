import unittest
from random import randint

from small_text_game.src.event import *


class EventTestCase(unittest.TestCase):
    def test_create_event_object(self):
        position = [randint(0, 100), randint(0, 100)]
        data = ['data']
        event = Event(position, data)
        self.assertIsNotNone(event)
        self.assertEqual(event.position, position)
        self.assertEqual(event.data, data)
        self.assertEqual(event.name, 'abstract')

    def test_create_kick_event_object(self):
        position = [randint(0, 100), randint(0, 100)]
        data = ['data']
        event = KickEvent(position, data)
        self.assertIsNotNone(event)
        self.assertIsInstance(event, Event)
        self.assertEqual(event.name, 'kick')

    def test_create_message_event_object(self):
        position = [randint(0, 100), randint(0, 100)]
        data = ['data']
        event = MessageEvent(position, data)
        self.assertIsNotNone(event)
        self.assertIsInstance(event, Event)
        self.assertEqual(event.name, 'message')
        self.assertIsInstance(event.data, list)

        data = 'data'
        event = MessageEvent(position, data)
        self.assertIsInstance(event.data, list)


if __name__ == '__main__':
    unittest.main()
