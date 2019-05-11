from unittest import TestCase, main
from adt_playlist import PlayList
from data_module import Song


class TestPlayList(TestCase):
    def setUp(self):
        self.playlist1 = PlayList()
        self.playlist2 = PlayList()
        self.playlist3 = PlayList()

        self.song1 = Song()
        self.song2 = Song()
        self.song3 = Song()
        self.song4 = Song()

        self.song1.track_id = 123
        self.song1.artist = 'Adele'
        self.song1.track_name = 'Hello'

        self.song2.track_id = 124
        self.song2.artist = 'Aerosmith'
        self.song2.track_name = 'Dream on'

        self.song3.track_id = 125
        self.song3.artist = 'Led Zeppelin'
        self.song3.track_name = 'Immigrant song'

        self.song4.track_id = 126
        self.song4.artist = 'OneRepublic'
        self.song4.track_name = 'Love Runs Out'

    def test_a_add(self):
        self.playlist1.add(self.song1)
        self.playlist1.add(self.song2)
        self.playlist1.add(self.song1)

        self.playlist2.add(self.song1)
        self.playlist2.add(self.song2)
        self.assertEqual(self.playlist1._data, self.playlist2._data, 'Перевірка на додавання однакових треків')

    def test_b_clear(self):
        self.playlist1.add(self.song1)
        self.playlist1.add(self.song2)

        self.playlist2.add(self.song1)
        self.playlist2.add(self.song2)

        current_status = self.playlist1._data
        self.playlist1.clear()

        self.assertNotEqual(self.playlist1._data, current_status, 'Перевірка на очищення плейлиста')
        self.assertEqual(self.playlist1._clipboard[-1], current_status, 'Перевірка стану буфера обміну')

    def test_c_pull_back(self):
        self.playlist1.add(self.song1)
        self.playlist1.add(self.song2)

        self.playlist2.add(self.song1)
        self.playlist2.add(self.song2)

        self.playlist1.clear()

        self.playlist1.pull_back()

        self.assertEqual(self.playlist1._data, self.playlist2._data, 'Перевірка буфера обміну')

    def test_d_change(self):
        self.playlist1.add(self.song1)
        self.playlist1.add(self.song2)

        self.playlist2.add(self.song1)
        self.playlist2.add(self.song2)

        self.playlist1[0] = self.song3

        self.assertEqual(self.playlist1._data[0], self.song3, 'Перевірка заміни треку')

    def test_e_delete(self):
        self.playlist1.add(self.song1)
        self.playlist1.add(self.song2)

        self.playlist2.add(self.song1)
        self.playlist2.add(self.song2)

        self.playlist1[0] = self.song3

        deleted_song = self.playlist1.remove(0)

        self.assertEqual(self.playlist1._data[0], self.song2, 'Перевірка стану плейлиста')
        self.assertEqual(deleted_song, self.song3, 'Перевірка видаленого треку')

    def test_f_change_of_2_tracks(self):
        self.playlist1.add(self.song2)
        self.playlist1.add(self.song1)
        self.playlist1.add(self.song3)
        self.playlist1.add(self.song4)

        self.playlist1.change_position(0, 3)

        self.assertEqual(self.playlist1._data[0], self.song4, 'Перевірка заміни')

    def test_g_equal(self):
        self.playlist1.add(self.song4)
        self.playlist1.add(self.song1)
        self.playlist1.add(self.song3)
        self.playlist1.add(self.song2)

        self.playlist3.add(self.song4)
        self.playlist3.add(self.song1)
        self.playlist3.add(self.song3)
        self.playlist3.add(self.song2)

        self.assertEqual(self.playlist1, self.playlist3, 'Перевірка на рівність')

        self.playlist3.change_position(0, 1)

        self.assertNotEqual(self.playlist1, self.playlist3, 'Перевірка на рівність')


if __name__ == '__main__':
    main()
