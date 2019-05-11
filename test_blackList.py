from unittest import TestCase, main
from adt_blacklist import BlackList
from data_module import Song


class TestBlackList(TestCase):
    def setUp(self):
        self.blacklist1 = BlackList()
        self.blacklist2 = BlackList()

        self.song1 = Song()
        self.song2 = Song()
        self.song3 = Song()

        self.song1.track_id = 123
        self.song1.artist = 'Adele'
        self.song1.track_name = 'Hello'

        self.song2.track_id = 124
        self.song2.artist = 'Aerosmith'
        self.song2.track_name = 'Dream on'

        self.song3.track_id = 125
        self.song3.artist = 'Led Zeppelin'
        self.song3.track_name = 'Immigrant song'

    def test_a_add(self):
        self.blacklist1.add_song(self.song1)
        self.blacklist1.add_song(self.song2)
        self.blacklist1.add_song(self.song1)

        self.blacklist2.add_song(self.song1)
        self.blacklist2.add_song(self.song2)
        self.assertEqual(self.blacklist1._songs_data, self.blacklist2._songs_data,
                         'Перевірка на додавання однакових треків')

    def test_b_clear(self):
        self.blacklist1.add_song(self.song1)
        self.blacklist1.add_song(self.song2)

        self.blacklist2.add_song(self.song1)
        self.blacklist2.add_song(self.song2)

        current_status = self.blacklist1._songs_data
        self.blacklist1.clear()

        self.assertNotEqual(self.blacklist1._songs_data, current_status, 'Перевірка на очищення чорного списку')
        self.assertEqual(self.blacklist1._songs_data, [], 'Перевірка на стан чорного чписку')

    def test_d_change(self):
        self.blacklist1.add_song(self.song1)
        self.blacklist1.add_song(self.song2)

        self.blacklist2.add_song(self.song1)
        self.blacklist2.add_song(self.song2)

        self.blacklist1[0] = self.song3

        self.assertEqual(self.blacklist1._songs_data[0], self.song3, 'Перевірка заміни треку')

    def test_e_delete(self):
        self.blacklist1.add_song(self.song1)
        self.blacklist1.add_song(self.song2)

        self.blacklist2.add_song(self.song1)
        self.blacklist2.add_song(self.song2)

        self.blacklist1 [0] = self.song3

        deleted_song = self.blacklist1.remove_song(0)

        self.assertEqual(self.blacklist1._songs_data [0], self.song2, 'Перевірка стану плейлиста')
        self.assertEqual(deleted_song, self.song3, 'Перевірка видаленого треку')

    def test_g_equal(self):
        self.blacklist1.add_song(self.song1)
        self.blacklist1.add_song(self.song3)
        self.blacklist1.add_song(self.song2)

        self.blacklist2.add_song(self.song1)
        self.blacklist2.add_song(self.song3)
        self.blacklist2.add_song(self.song2)

        self.assertEqual(self.blacklist1, self.blacklist2, 'Перевірка на рівність')

        genre = 'Pop'
        self.blacklist1.add_genre(genre)

        self.assertNotEqual(self.blacklist1, self.blacklist2, 'Перевірка на рівність')


if __name__ == '__main__':
    main()

