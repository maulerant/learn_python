import unittest
from random import randint
from unittest.mock import patch

from small_text_game.src.camera import Camera
from small_text_game.src.map import Map
from small_text_game.src.options import *


class CameraTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.camera = Camera()

    def test_make_camera_object(self):
        self.assertIsNotNone(self.camera)

    @patch('small_text_game.src.map.Map')
    @patch('small_text_game.src.user.User')
    @patch('builtins.print')
    def test_show_map(self, patched_print, MockUser, MockMap):
        width, height = randint(1, 100), randint(1, 100)
        patched_print.return_value = ''
        MockMap.size.return_value = [width, height]
        MockUser.position = [2, 2]
        self.camera.show(MockMap, MockUser, SMOG_RADIUS)
        MockMap.size.assert_called_with()
        self.assertEqual(patched_print.call_count, height + 2)

    def test_apply_smog(self):
        map = Map()
        width, height = 5, 5
        map.generate(width, height, EMPTY)
        position = [2, 2]
        map.map = [
            [EMPTY for x in range(width)],
            [TREASURE for x in range(width)],
            [LETTER for x in range(width)],
            [TREE for x in range(width)],
            [EMPTY for x in range(width)],
        ]
        position = [2, 2]
        expected = [
            list('#####'),
            list('#$$$#'),
            list('#@@@#'),
            list('#TTT#'),
            list('#####'),
        ]
        self.assertEqual(self.camera.apply_smog(map, position, 1), expected)

        position = [1, 2]
        expected = [
            list('#####'),
            list('$$$##'),
            list('@@@##'),
            list('TTT##'),
            list('#####'),
        ]
        self.assertEqual(self.camera.apply_smog(map, position, 1), expected)

        position = [1, 1]
        expected = [
            list('   ##'),
            list('$$$##'),
            list('@@@##'),
            list('#####'),
            list('#####'),
        ]
        self.assertEqual(self.camera.apply_smog(map, position, 1), expected)


if __name__ == '__main__':
    unittest.main()
