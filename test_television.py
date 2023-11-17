import unittest
from television import Television
class TestTelevision(unittest.TestCase):

    def test_init(self):
        tv = Television()
        self.assertEqual(tv.__str__(), 'Power = False, Channel = 0, Volume = 0')

    def test_power(self):
        pass

    def test_mute(self):
        pass

    def test_channel_up(self):
        pass

    def test_channel_down(self):
        pass

    def test_volume_up(self):
        pass

    def test_volume_down(self):
        pass