import pytest
from television import Television


class TestTelevision:

    def test_init(self):
        tv = Television()
        #self.assertEqual(tv.__str__(), 'Power = False, Channel = 0, Volume = 0')
        assert 'Power = False, Channel = 0, Volume = 0' in tv.__str__()

    def test_power(self):
        tv = Television()
        tv.power()
        #self.assertEqual(tv.__str__(), 'Power = True, Channel = 0, Volume = 0')
        assert 'True' in tv.__str__()
        tv.power()
        #self.assertEqual(tv.__str__(), 'Power = False, Channel = 0, Volume = 0')
        assert 'False' in tv.__str__()

    def test_mute(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.mute()
        assert 'Power = True, Channel = 0, Volume = 0' in tv.__str__()
        tv.mute()
        assert 'Power = True, Channel = 0, Volume = 1' in tv.__str__()
        tv.mute()
        tv.power()
        assert 'Power = False, Channel = 0, Volume = 0' in tv.__str__()
        tv.power()
        tv.mute()
        tv.power()
        assert 'Power = False, Channel = 0, Volume = 1' in tv.__str__()

    def test_channel_up(self):
        tv = Television()
        tv.channel_up()
        assert 'Power = False, Channel = 0, Volume = 0' in tv.__str__()
        tv.power()
        tv.channel_up()
        assert 'Power = True, Channel = 1, Volume = 0' in tv.__str__()
        tv.channel_up()
        tv.channel_up()
        tv.channel_up()
        assert 'Power = True, Channel = 0, Volume = 0' in tv.__str__()

    def test_channel_down(self):
        tv = Television()
        tv.channel_down()
        assert 'Power = False, Channel = 0, Volume = 0' in tv.__str__()
        tv.power()
        tv.channel_down()
        assert 'Power = True, Channel = 3, Volume = 0' in tv.__str__()

    def test_volume_up(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.power()
        tv.volume_up()
        assert 'Power = False, Channel = 0, Volume = 1' in tv.__str__()
        tv.power()
        tv.volume_up()
        assert 'Power = True, Channel = 0, Volume = 2' in tv.__str__()
        tv.mute()
        tv.volume_up()
        assert 'Power = True, Channel = 0, Volume = 0' in tv.__str__()
        tv.mute()
        tv.volume_up()
        assert 'Power = True, Channel = 0, Volume = 2' in tv.__str__()

    def test_volume_down(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.power()
        tv.volume_down()
        assert 'Power = False, Channel = 0, Volume = 1' in tv.__str__()
        tv.power()
        tv.volume_down()
        assert 'Power = True, Channel = 0, Volume = 0' in tv.__str__()
        tv.volume_up()
        tv.mute()
        tv.volume_down()
        assert 'Power = True, Channel = 0, Volume = 0' in tv.__str__()
        tv.mute()
        tv.volume_down()
        tv.volume_down()
        assert 'Power = True, Channel = 0, Volume = 0' in tv.__str__()
